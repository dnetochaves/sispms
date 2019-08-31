from django.shortcuts import render, redirect
from .models import Feed
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import FeedForm
from usuario.models import Usuario


def home(request):
    return render(request, 'home.html')


def construction(request):
    return render(request, 'home/construction.html')


def teste_bootstrap(request):
    return render(request, 'home/teste_bootstrap.html')


def feed(request):
    busca = request.GET.get('pesquisa', None)
    # TODO: Remover codigo repetido
    busca_feed = Feed.objects.filter(UsuarioFeed_id=request.user)

    for feed in busca_feed:
        id_setor = feed.SetorFeed.id

   # TODO: Correção a lista da erro quando não tem feed
    if busca:
        feed = Feed.objects.filter(Titulo=busca)
    else:
        feed = Feed.objects.filter(SetorFeed=id_setor)

    return render(request, 'home/feed.html', {'feed': feed})


@login_required
def add_feed(request):
    # TODO: Remover codigo repetido
    busca_feed = Feed.objects.filter(UsuarioFeed_id=request.user)

    for feed in busca_feed:
        id_setor = feed.SetorFeed.id

    form = FeedForm(request.POST or None)
    if form.is_valid():
        formulario = form.save(commit=False)
        formulario.UsuarioFeed = request.user
        formulario.SetorFeed_id = id_setor
        formulario.save()
        return redirect('/home/feed')
    return render(request, 'home/add_feed.html', {'form': form})
