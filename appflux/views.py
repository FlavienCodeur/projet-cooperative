from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from appflux.models import Entrepreneur, Fichier
from . import models
from django.views.generic import DetailView, CreateView, UpdateView
from appflux.forms import EntrepreneurForm, EntrepreneurFiltre, FichierForm
from django.urls import reverse_lazy , reverse
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse


@login_required
def home(request):
    liste = Entrepreneur.objects.all()

    if request.method == "POST":
        form = EntrepreneurFiltre(request.POST)
        if form.is_valid():
            base_url = reverse('home')
            query_string = urlencode(form.cleaned_data)
            url = '{}?{}'.format(base_url, query_string)
            return redirect (url)
    else:
        form = EntrepreneurFiltre()
        nom_form = request.GET.get("nom","")
        prenom_form = request.GET.get("prenom","")
        structure_form = request.GET.get("structure","")
        if nom_form is not None:
            liste = liste.filter(nom__icontains=nom_form)
            form.fields['nom'].initial = nom_form
        if prenom_form is not None:
            liste = liste.filter(prenom__icontains=prenom_form)
            form.fields['prenom'].initial = prenom_form
        if structure_form is not None:
            liste = liste.filter(structure__icontains=structure_form)
            form.fields['structure'].initial = structure_form

    return render(request, "appflux/home.html", locals())


class CreerEntrepreneur(LoginRequiredMixin, CreateView):
    model = Entrepreneur
    form_class =  EntrepreneurForm
    template_name = 'appflux/form.html'

    def get_success_url(self):
        return reverse_lazy("home")
    

class UpdateEntrepreneur(LoginRequiredMixin, UpdateView):
    model = Entrepreneur
    form_class =  EntrepreneurForm
    template_name = 'appflux/form.html'

    def get_success_url(self):
        return reverse_lazy("home")
    

@login_required
def detail_entrepreneur(request, entrepreneur_id):
    entrepreneur = get_object_or_404(Entrepreneur, id=entrepreneur_id)
    return render(request, 'appflux/entrepreneur_detail.html', {'entrepreneur': entrepreneur,})



def telecharger_fichier(request, entrepreneur_id):
    entrepreneur = get_object_or_404(Entrepreneur, pk=entrepreneur_id)

    if request.method == 'POST':
        form = FichierForm(request.POST, request.FILES)
        if form.is_valid():
            fichier = form.save(commit=False)
            fichier.entrepreneur = entrepreneur
            fichier.save()
            return redirect('entrepreneur_detail', entrepreneur_id=entrepreneur.id)
    else:
        form = FichierForm()

    return render(request, 'appflux/telecharger_fichier.html', {'entrepreneur': entrepreneur, 'form': form})

def fichiers(request, entrepreneur_id):
    entrepreneur = get_object_or_404(Entrepreneur, id=entrepreneur_id)
    fichiers = Fichier.objects.filter(entrepreneur=entrepreneur).order_by("-date_created")
    return render(request, 'appflux/fichiers.html', {'entrepreneur': entrepreneur, 'fichiers': fichiers})