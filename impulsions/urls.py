"""impulsions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
import authentification.views 
import appflux.views 
from django.contrib.auth.views import (LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView)
from django.conf.urls.static import static
from django.contrib.auth import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view( template_name="authentification/login.html",redirect_authenticated_user=True,),name ="login"),
    path("home/", appflux.views.home, name="home"),
    path("change-password",PasswordChangeView.as_view(template_name="authentification/password_change_form.html"),name="password_change",),
    path("change-password-done/",PasswordChangeDoneView.as_view(template_name="authentification/password_change_done.html"),name="password_change_done",),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('profile/',authentification.views.profile , name='profile'),
    path('reset_password/', views.PasswordResetView.as_view(template_name ="authentification/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', views.PasswordResetDoneView.as_view(template_name="authentification/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(template_name="authentification/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/',views.PasswordResetCompleteView.as_view(template_name="authentification/password_reset_done.html"), name="password_reset_complete"),
    path('home/<int:entrepreneur_id>/', appflux.views.detail_entrepreneur ,name="entrepreneur_detail"),
    path('home/create', appflux.views.CreerEntrepreneur.as_view(), name='creer_personne'),
    path('home/<int:pk>/update/', appflux.views.UpdateEntrepreneur.as_view(), name='update_entrepreneur'),
    path('home/<int:entrepreneur_id>/telecharger_fichier/', appflux.views.telecharger_fichier, name='telecharger_fichier'),
    path('home/<int:entrepreneur_id>/fichiers/', appflux.views.fichiers, name='fichiers'),
    path('home/<int:entrepreneur_id>/creer-rendezvous/', appflux.views.creer_rendezvous, name='creer-rendezvous'),
    path('home/<int:entrepreneur_id>/rendezvous/', appflux.views.rendezvous_list, name='rendezvous_list'),
    path('home/<int:entrepreneur_id>/rendezvous/<int:rendezvous_id>/', appflux.views.rendezvous_detail, name='rendez_detail'),
    path('home/<int:entrepreneur_id>/rendezvous/<int:rendezvous_id>/update/', appflux.views.rendez_vous_update, name='rendezvous_update'),
    path('rendezvous/', appflux.views.index, name='rendezvous'),
     path('rendezvous/create', appflux.views.rendezvous_new, name='creer_rendezvous'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)