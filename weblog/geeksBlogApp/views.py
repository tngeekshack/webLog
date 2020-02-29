from django.shortcuts import render
from .models import Post

def post_list(request):
    contents = {
    'posts': Post.objects.all()
} 
    return render(request, 'geeksBlogApp/post_list.html' ,contents)

