from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, Category
from contact.forms import QuoteRequestForm
from django.core.mail import send_mail
from django.conf import settings
from contact.models import QuoteRequest
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives





def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(is_featured=True).order_by('-created_at')

    selected_categories = request.GET.getlist('category')
    price_max = request.GET.get('price_max', None)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if selected_categories:
        products = products.filter(category__slug__in=selected_categories)

    if price_max:
        products = products.filter(price__lte=price_max)

    context = {
        'products': products,
        'categories': categories,
        'selected_categories': selected_categories,
        'price_max': price_max,
    }

    return render(request, 'products/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    images = product.images.all()
    features = product.features.all()
    domain = 'http://127.0.0.1:8000'

    
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST, initial={'product': product})
        if form.is_valid():
            quote = form.save(commit=False)
            quote.product = product
            quote.save()

            # Send email notification
            admin_email = 'mayankrajoriya2004@gmail.com'
            subject = f"Quote Request for {product.name}"
            
            # m = /home/mayank-rajoriya/StoneCraft/handicraft/products/templates/email/qoute_request_email.html
            html_message = render_to_string('email/qoute_request_email.html', {
                'product': product,
                'quote': quote,
                'domain': domain,
            })
            

            # email = EmailMessage(
            #     subject=subject,
            #     body=email_body,
            #     from_email=settings.EMAIL_HOST_USER,
            #     to=[admin_email],
            # )


            email = EmailMultiAlternatives(subject,
                                            html_message,
                                            settings.EMAIL_HOST_USER,
                                            [admin_email])

            email.content_subtype = "html"
            email.send(fail_silently=False)


           
            messages.success(request, "Thank you for your quote request! We'll contact you soon.")
            return redirect('product_detail', slug=slug)
    else:
        form = QuoteRequestForm(initial={'product': product})
        
    return render(request, 'products/product_detail.html', {'product': product, 'form': form, 'images': images, 'features': features})
