
from django.views.generic import TemplateView

from .models import Post
from .forms import PostForm,DeletePostForm
from rest_framework import generics, renderers, status
from rest_framework.response import Response
from .serializers import PostSerializers

from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

class PostList(generics.ListCreateAPIView):

    queryset=Post.objects.all()
    serializer_class=PostSerializers



   

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    
   
    queryset=Post.objects.all()
    serializer_class=PostSerializers

def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_update.html', {'form': form, 'post': post})
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = DeletePostForm(request.POST)
        if form.is_valid() and form.cleaned_data.get('confirm_delete'):
            post.delete()
            return redirect('post-list')
    else:
        form = DeletePostForm()
    
    return render(request, 'post_delete.html', {'post': post, 'form': form})

    



        
    
