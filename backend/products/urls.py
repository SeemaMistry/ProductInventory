from django.urls import path
from products import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products', views.product, name='product'),
    path('products/product_delete/<int:id>', views.product_delete, name='product_delete'),
]