from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    return render(request, 'blog2/post_list.html', {})

def post_musica(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog2/post_musica.html', {})

def post_foto(request):
    #post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog2/post_foto.html', {})
# Create your views here.
