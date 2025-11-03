from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact, name='contact'),
    # path('quote/<slug:product_slug>/', views.request_quote, name='request_quote'),
]
