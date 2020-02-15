from django.shortcuts import render, redirect
from .models import Meme
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

@login_required(login_url="/accounts/login/")
def meme_list(request):
    memes = Meme.objects.all().order_by('date')
    return render(request, 'memez/meme_list.html', {'memes': memes})


def meme_detail(request, slug):
    meme = Meme.objects.get(slug=slug)
    return render(request, 'memez/meme_detail.html', {'meme':meme})


@login_required(login_url="/accounts/login/")
def meme_create(request):
    if request.method == 'POST':
        form = forms.CreateMeme(request.POST, request.FILES)
        if form.is_valid():
            # save meme to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('memes:list')
    else:     
        form = forms.CreateMeme()
    return render(request, 'memez/memez_create.html', {'form':form})