from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from appflux.models import Entrepreneur
from . import models
from django.views.generic import DetailView


@login_required
def home(request):
    liste = Entrepreneur.objects.all()
    return render(request, "appflux/home.html", context={"liste": liste})

