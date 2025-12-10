from django.shortcuts import render
from products.models import Category
from .models import HeroSection
from django.core.files.storage import ContentFile
from django.http import HttpResponse
import requests

# # Create your views here.
def Test(request):
    r = requests.get("https://via.placeholder.com/150")
    if r.status_code != 200:
        return HttpResponse("Failed to download image", status=500)
        img = ContentFile(r.content, name="test.jpg")
    
    try:
        import Cloudinary.uploader
        Cloudinary.uploader.upload(img, folder="test")
        return HttpResponse("Image uploaded successfully", status=200)
    except Exception as e:
        return HttpResponse(f"uploaded failed {e}", status=500)
     

def home(request):
    categories = Category.objects.all() # या जो भी आपकी मौजूदा लॉजिक है
    
    # सक्रिय और सबसे नया हीरो सेक्शन डेटा प्राप्त करें
    hero_section = HeroSection.objects.filter(is_active=True).first()

    context = {
        'categories': categories,
        'hero': hero_section, # हीरो डेटा को कॉन्टेक्स्ट में जोड़ें
    }
    return render(request, 'home.html', context)
