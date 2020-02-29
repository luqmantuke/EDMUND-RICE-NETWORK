from django.urls import  path

from . import  views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about_us, name='about_us'),
    path('donations/', views.donations, name='donations'),
]