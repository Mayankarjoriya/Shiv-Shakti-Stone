from django.urls import path
from . import views

urlpatterns = [
    # path('contact/', views.contact_view, name='contact'),
    # path('request-quote/', views.request_quote_view, name='request_quote'),
    path('', views.home, name='home'),
 ]