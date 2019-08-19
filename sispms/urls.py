"""sispms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuario import urls as usuario_urls
from home import urls as home_urls
from colaborador import urls as colaborador_urls
from setor import urls as setor_urls
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django .conf.urls.static import static

urlpatterns = [
    path('', include(home_urls)),
    path('login/', LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('usuario/', include(usuario_urls)),
    path('colaborador/', include(colaborador_urls)),
    path('setor/', include(setor_urls)),
    path('admin/', admin.site.urls),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.sites.site.site_header = 'SisPms'
admin.site.index_title = 'Administação'
admin.site.site_title = 'v.3.2.5 - Release'