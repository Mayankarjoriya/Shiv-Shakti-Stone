from django.db import models
from products.models import Product  # circular import ok if apps installed in INSTALLED_APPS order

# models :-

class QuoteRequest(models.Model):
    product = models.ForeignKey(Product, related_name='quotes', on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    mobile = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=30, default='new')  # new / contacted / closed
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.name} — {self.product.name if self.product else 'Custom request'}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    # address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.name} — {self.email or self.mobile}"
