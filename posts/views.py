from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'base.html', context)

def create(request):
    context = {
        'page': 'create'
    }
    return render(request, 'base.html', context)

def detail(request):
    context = {
        'page': 'detail'
    }
    return render(request, 'base.html', context)

def update(request):
    context = {
        'page': 'update'
    }
    return render(request, 'base.html', context)

def delete(request):
    context = {
        'page': 'delete'
    }
    return render(request, 'base.html', context)



