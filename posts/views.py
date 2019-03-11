from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,redirect
from django.contrib import messages
from django.http import HttpResponse, Http404
from .models import Post
from .forms import PostForm

# Create your views here.
def list(request):
    queryset = Post.objects.all()
    context = {
        'posts' : queryset
    }
    return render(request, 'list.html', context)

def create(request):
    if not request.user.is_authenticated():
        raise Http404
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Post created succesfully')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

def detail(request, id=id):
    instance = get_object_or_404(Post, id=id)
    context = {
        'page': 'detail',
        'instance': instance
    }
    return render(request, 'detail.html', context)

def update(request, id=id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None,request.FILES or None, instance=instance)
    if form.is_valid():
        new_instance = form.save(commit=False)
        new_instance.save()
        messages.success(request, 'Post updated succesfully')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form': form
    }
    return render(request, 'update.html', context)

def delete(request, id=id):
    instance  = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, 'delete succesfull')
    return redirect('posts:list')

