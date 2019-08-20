from django.urls import path
from .views import home
from .views import teste_bootstrap
from .views import construction
from .views import feed

urlpatterns = [
    path('', home, name="home"),
    path('teste_bootstrap', teste_bootstrap, name="teste_bootstrap"),
    path('construction', construction, name="construction"),
    path('feed', feed, name="feed"),
]
