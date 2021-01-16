from django.shortcuts import render

def show(request):
    return render(request, 'djangolab/index.html')

def about(request):
    return render(request, 'djangolab/about.html')


