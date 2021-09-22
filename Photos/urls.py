from django.urls import path
from . import views 

# set url patterns
# Make the gallery your home page, so ''
# Identify the photos by pk


urlpatterns = [
    path('', views.gallery, name = 'gallery'),
    path('photo/<str:pk>/', views.viewPhoto, name = 'photo'),
    path('add/', views.addPhoto, name = 'add'),
]
