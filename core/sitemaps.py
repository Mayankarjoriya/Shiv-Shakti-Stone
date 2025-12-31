from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product, Category

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'contact', 'product_list']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return reverse('product_detail', kwargs={'slug': obj.slug})

class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return reverse('product_list', kwargs={'category_slug': obj.slug})