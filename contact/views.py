from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# from .forms import ContactMessageForm
from .models import ContactMessage
from django.conf import settings
from products.models import Product
from .models import QuoteRequest
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')


        if not name or not message:
            messages.error(request, "Please fill in all required fields.")
            return redirect('/contact')

        # save to DB
        # ContactMessage.objects.create(
        #     name=name,
        #     email=email,
        #     mobile=mobile,
        #     message=message
        # )

        html_content = render_to_string('emails/contact_email.html', {
            'name': name,
            'email': email,
            'mobile': mobile,
            'message': message,
            # 'image_url': f"{settings.STATIC_URL}images/logo.png",  # Example image
        })

        # send email to admin
        admin_email = settings.SERVER_EMAIL

        subject = f"New contact meesage from- {name}"


        email_msg = EmailMultiAlternatives(subject,
                                            message,
                                              settings.DEFAULT_FROM_EMAIL,
                                                [admin_email],
                                                fail_silently=False,)
        email_msg.attach_alternative(html_content, "text/html")

        email_msg.send()
       

        messages.success(request, 'Your message has been sent')
        

    return render(request, 'contact/contact.html')

