from django.urls import path
from . import views

urlpatterns = [
    path('', views.webscrap, name='webscrap'),
    path('xpath/', views.xpath, name='xpath'),
    path('zajecia/', views.zajecia, name='zajecia')
]