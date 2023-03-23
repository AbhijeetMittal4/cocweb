from django.shortcuts import render
from .models import Post

def mvhome(request):
    return render(request , "mvhome.html")

def blizlalo(request):
    post = Post.objects.get(pk="Blizzard Lalo")
    context = {"post":post}
    return render(request , "blizlalo.html" , context)