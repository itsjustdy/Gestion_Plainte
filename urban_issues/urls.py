from django.contrib import admin
from django.urls import path, include
from issues import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('issues/', include('issues.urls')),
    path('', views.signup, name='home'),  # Redirige la page d'accueil vers la page d'inscription
    path('accounts/', include('django.contrib.auth.urls')),  # Ajout des URL d'authentification
]