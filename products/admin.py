from django.contrib import admin
from .models import Category, Product, ProductImage, ProductFeature




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}


class ProductImageInline(admin.TabularInline):  # ❌ decorator hatao
    model = ProductImage
    extra = 1


class ProductFeatureInline(admin.TabularInline):
    model = ProductFeature
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'material', 'shape', 'color', 'category', 'is_featured', 'created_at')
    list_filter = ('category', 'is_featured')
    search_fields = ('name', 'description')
    inlines = [ProductImageInline, ProductFeatureInline]
    prepopulated_fields = {"slug": ("name",)}


# optional: agar ProductImage alag se bhi dikhana ho admin mein
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
