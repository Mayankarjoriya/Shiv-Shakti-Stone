from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Category
from contact.forms import QuoteRequestForm
from django.core.mail import send_mail
from django.conf import settings
from contact.models import QuoteRequest
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.db.models import Max, Q




def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(is_featured=True).order_by('-created_at')
    selected_categories = request.GET.getlist('category')
    price_max = request.GET.get('price_max', None)
    min_price = request.GET.get('min_price', None)
    search_query = request.GET.get('search')

    # Calculate the max price , Default 10000
    price_aggregate = Product.objects.aggregate(Max('price'))
    global_max_price = price_aggregate['price__max'] or 10000

    # filter by Category
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )


    if selected_categories:
        products = products.filter(category__slug__in=selected_categories)

    if price_max:
        products = products.filter(price__lte=price_max)
    if min_price:
        products = products.filter(price__gte=min_price)

    context = {
        'products': products,
        'categories': categories,
        'selected_categories': selected_categories,
        'price_max': price_max,
        'global_max_price': global_max_price,
        'selected_min': min_price,
        'selected_max': price_max,
        'search_query':search_query,

    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = product.images.all()
    features = product.features.all()
    # ISSUE: Hardcoded domain. Use request.build_absolute_uri or settings.SITE_URL for flexibility.
    domain = 'http://127.0.0.1:8000'

    
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST, initial={'product': product})
        if form.is_valid():
            quote = form.save(commit=False)
            quote.product = product
            quote.save()

            # Send email notification
            admin_email = settings.ADMIN_EMAIL
            subject = f"Quote Request for {product.name}"
            
            # m = /home/mayank-rajoriya/StoneCraft/handicraft/products/templates/email/qoute_request_email.html
            html_message = render_to_string('email/qoute_request_email.html', {
                'product': product,
                'quote': quote,
                'domain': domain,
            })
            text_content = f"New quote request for {product.name}"
            

            # email = EmailMessage(
            #     subject=subject,
            #     body=email_body,
            #     from_email=settings.EMAIL_HOST_USER,
            #     to=[admin_email],
            # )


            email = EmailMultiAlternatives(subject,
                                            text_content,
                                            settings.DEFAULT_FROM_EMAIL,
                                            [admin_email],
                                            )

            # email.content_subtype = "html"
            email.attach_alternative(html_message, "text/html")
            # POTENTIAL ERROR: email.send() might fail without being logged or handled gracefully.
            # AAPKE LIYE: fail_silently=False stands, but consider adding try-except for production stability.
            email.send(fail_silently=False)


           
            messages.success(request, "Thank you for your quote request! We'll contact you soon.")
            return redirect('product_detail', slug=slug)
    else:
        form = QuoteRequestForm(initial={'product': product})
        
    return render(request, 'products/product_detail.html', {'product': product, 'form': form, 'images': images, 'features': features})
