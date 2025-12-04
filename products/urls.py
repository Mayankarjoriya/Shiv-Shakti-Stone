from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list'),
    path('<slug:slug>/', views.product_detail, name='product_detail'),
]

# from rest_framework.routers import DefaultRouter
# from .views import CategoryViewSet, ProductViewSet
# from django.urls import path, include

# router = DefaultRouter()
# router.register(r'categories', CategoryViewSet, basename='category')
# router.register(r'products', ProductViewSet, basename='product')

# urlpatterns = [
#     path('', include(router.urls)),
# ]
