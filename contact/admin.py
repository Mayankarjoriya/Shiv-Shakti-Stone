from django.contrib import admin
from .models import QuoteRequest, ContactMessage

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','product','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('name','mobile','email','product__name')
    readonly_fields = ('created_at',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','created_at')
    search_fields = ('name','email','mobile')
    readonly_fields = ('created_at',)
