from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_products),
    path('products/create/', views.create_product),
    
    path('', views.index),
    
]