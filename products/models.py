from django.db import models
from django.utils.text import slugify
import uuid

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='category', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Order_quantity = models.CharField(max_length=100,blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    shape = models.CharField(blank=True, null=True)
    height = models.CharField(blank=True, null=True)
    usage_application = models.CharField(blank=True, null=True)
    model_number= models.CharField()
    country_of_origin = models.CharField(max_length=100, blank=True, null=True)
    production_capacity = models.CharField(max_length=200, blank=True, null=True)
    delivery_time = models.CharField(max_length=200, blank=True, null=True)
    packaging_details = models.CharField(max_length=200, blank=True, null=True)
    brochure = models.FileField(upload_to='brochures/', blank=True, null=True)
    material = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)
    dimensions = models.CharField(max_length=120, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product/gallery/', blank=True, null=True)

    class Meta:
        ordering = ('-is_featured', '-created_at', 'name')

        

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)[:200]
            slug = base_slug
            # Appending a UUID to make sure the slug is unique
            while Product.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to='products/static/products/gallery/')

    def __str__(self):
        return f"Image for {self.product.name}"


class ProductFeature(models.Model):
    product = models.ForeignKey('Product', related_name='features', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}: {self.value}"
    
