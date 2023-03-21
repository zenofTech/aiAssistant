from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .engine import chatengine

def home(request):
    try:
        if request.method == 'POST':
            context = chatengine(request)
            return render(request, 'home.html', context)
        else:
            return render(request, 'home.html')
    except:
        return redirect('error')

def error_handler(request):
        return render(request, 'error.html')