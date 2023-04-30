from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.Index, name='index'),
    path('producto/<int:producto_id>/', views.Product, name='producto'),
    path('category/<int:category_id>/', views.Category, name='category'),
]
