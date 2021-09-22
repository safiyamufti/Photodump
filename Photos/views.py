from django.shortcuts import render
from .models import Category, Photo

# Create your views here.
# creating some function based views here

def gallery(request):
    categories = Category.objects.all()
    photos = Photo.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'Photos/gallery.html', context)
    
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'Photos/image.html', {'photo': photo})

def addPhoto(request):
    return render(request, 'Photos/add.html')



    

