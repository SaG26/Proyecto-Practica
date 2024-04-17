from django.shortcuts import render, redirect
from .models import Post, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def feed(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'social/feed.html', context)

def profile(request):
    return render(request, 'social/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario {username} fue creado correctamente.')
            return redirect('feed')
        else:
            messages.error(request, f'Error en la creacion')
    else: 
        form = UserRegisterForm


    context = { 'form' : form}
    return render(request, 'social/register.html', context)