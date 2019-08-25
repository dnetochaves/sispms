from django.shortcuts import render, redirect
from .models import Feed
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import FeedForm


def home(request):
    return render(request, 'home.html')


def construction(request):
    return render(request, 'home/construction.html')


def teste_bootstrap(request):
    return render(request, 'home/teste_bootstrap.html')


def feed(request):
    # return render(request, 'home/feed.html')
    busca = request.GET.get('pesquisa', None)

    if busca:
        # usuarios = Usuario.objects.all()
        feed = Feed.objects.all()
    else:
        feed = Feed.objects.all()

    return render(request, 'home/feed.html', {'feed': feed})


@login_required
def add_feed(request):
    form = FeedForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/home/feed')
    return render(request, 'home/add_feed.html', {'form': form})
