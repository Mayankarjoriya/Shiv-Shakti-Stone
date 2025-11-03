from django.shortcuts import render
from products.models import Category
from .models import HeroSection

# # Create your views here.
# def home(request):
#     categories = Category.objects.all()
#     hero_section = HeroSection.objects.filter(is_active=True).first()
#     context = {
#         'categories': categories
#         'hero': hero_section
#     }
#     return render(request, 'home.html', context)

# from django.shortcuts import render
# from products.models import Category
# from .models import HeroSection # इस लाइन को जोड़ें

def home(request):
    categories = Category.objects.all() # या जो भी आपकी मौजूदा लॉजिक है
    
    # सक्रिय और सबसे नया हीरो सेक्शन डेटा प्राप्त करें
    hero_section = HeroSection.objects.filter(is_active=True).first()

    context = {
        'categories': categories,
        'hero': hero_section, # हीरो डेटा को कॉन्टेक्स्ट में जोड़ें
    }
    return render(request, 'home.html', context)
