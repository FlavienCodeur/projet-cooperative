from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from appflux.models import Entrepreneur, Fichier, RendezVous
from . import models
from django.views.generic import DetailView, CreateView, UpdateView
from appflux.forms import EntrepreneurForm, EntrepreneurFiltre, FichierForm, RendezVousForm, RendezVousAnnuaire, RendezVousFiltre
from django.urls import reverse_lazy , reverse
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

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
            return redirect('entrepreneur_detail', entrepreneur_id=entrepreneur_id)
    else:
        form = FichierForm()

    return render(request, 'appflux/telecharger_fichier.html', {'entrepreneur': entrepreneur, 'form': form})

def fichiers(request, entrepreneur_id):
    entrepreneur = get_object_or_404(Entrepreneur, id=entrepreneur_id)
    fichiers = Fichier.objects.filter(entrepreneur=entrepreneur).order_by("-date_created")
    return render(request, 'appflux/fichiers.html', {'entrepreneur': entrepreneur, 'fichiers': fichiers})


def creer_rendezvous(request, entrepreneur_id):
    entrepreneur = Entrepreneur.objects.get(id=entrepreneur_id)
    if request.method == 'POST':
        rendezvous_form = RendezVousForm(request.POST)
        if rendezvous_form.is_valid():
            rendezvous = rendezvous_form.save(commit=False)
            rendezvous.entrepreneur = entrepreneur
            rendezvous.save()
            subject = f"Nouveau rendez-vous avec {entrepreneur.nom}"
            message = f"Bonjour {entrepreneur.nom} {entrepreneur.prenom},\n\nVous avez un nouveau rendez-vous le {rendezvous.date} à {rendezvous.heure}\n\n. Le sujet du rendez-vous est : {rendezvous.sujet}\n\n Le mode d\'entretien du rendez-vous est : {rendezvous.lieu}\n\n La nature du rendez-vous est : {rendezvous.nature}\n\n Les objectifs du rendez vous sont : {rendezvous.objectifs}\n\n Cordialement ZECOOP"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [entrepreneur.email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('entrepreneur_detail', entrepreneur_id=entrepreneur_id)
    else:
        rendezvous_form = RendezVousForm()
    context = {'entrepreneur': entrepreneur, 'rendezvous_form': rendezvous_form}
    return render(request, 'appflux/creer_rendezvous.html', context)


def rendezvous_list(request, entrepreneur_id):
    entrepreneur = get_object_or_404(Entrepreneur, pk=entrepreneur_id)
    rendezvous = RendezVous.objects.filter(entrepreneur=entrepreneur).order_by("-date")
    context = {'entrepreneur': entrepreneur, 'rendezvous': rendezvous}
    return render(request, 'appflux/rendezvous_list.html', context)


def rendezvous_detail(request, entrepreneur_id, rendezvous_id):
    entrepreneur = get_object_or_404(Entrepreneur, pk=entrepreneur_id)
    rendezvous = get_object_or_404(RendezVous, pk=rendezvous_id)
    if rendezvous.entrepreneur != entrepreneur:
        messages.error(request, 'Vous ne pouvez pas modifier ce rendez-vous.')
        return redirect('entrepreneur_detail', entrepreneur_id=entrepreneur_id)
    context = {'entrepreneur': entrepreneur, 'rendezvous': rendezvous}
    return render(request, 'appflux/rendezvous_detail.html', context)


def rendez_vous_update(request, entrepreneur_id, rendezvous_id):
    entrepreneur = get_object_or_404(Entrepreneur, pk=entrepreneur_id)
    rendezvous = get_object_or_404(RendezVous, pk=rendezvous_id)

    if request.method == "POST":
        form = RendezVousForm(request.POST, instance=rendezvous)
        if rendezvous.entrepreneur != entrepreneur:
            messages.error(request, 'Vous ne pouvez pas modifier ce rendezvous.')
            return redirect('home', entrepreneur_id=entrepreneur_id)
        
        if form.is_valid():
            rendezvous = form.save(commit=False)
            rendezvous.save()

            # send confirmation email to entrepreneur
            subject = f"Rendez-vous modifié avec {entrepreneur.nom}"
            message = f"Bonjour {entrepreneur.nom} {entrepreneur.prenom},\n\nVotre rendez-vous  a été modifié. Les nouvelles informations sont :\n\nNature : {rendezvous.nature}\nSujet : {rendezvous.sujet}\nObjectifs : {rendezvous.objectifs} \n\n\nLieu : {rendezvous.lieu}\nHeure : {rendezvous.heure}\nDate : {rendezvous.date}\n\nCordialement,\n ZECOOP"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [entrepreneur.email]
            send_mail(subject, message, from_email, recipient_list)

            return redirect('entrepreneur_detail', entrepreneur_id=entrepreneur_id)
    else:
        form = RendezVousForm(instance=rendezvous)

    context = {
        'entrepreneur': entrepreneur,
        'rendezvous': rendezvous,
        'form': form,
    }
    return render(request, 'appflux/rendezvous_update.html', context)

def index(request):
    liste = RendezVous.objects.all().select_related('entrepreneur').order_by("-date")

    if request.method == "POST":
        form = RendezVousFiltre(request.POST)
        if form.is_valid():
            try:
                base_url = reverse('rendezvous')
                query_string = urlencode(form.cleaned_data)
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
            except TypeError:
                query_string = urlencode({k: v for k, v in form.cleaned_data.items() if v is not None and v != ''})
                url = '{}?{}'.format(base_url, query_string)
                return redirect(url)
    else:
        form = RendezVousFiltre()
        nom_form = request.GET.get("nom", "")
        prenom_form = request.GET.get("prenom", "")
        date_min = request.GET.get("date_min", "")
        date_max = request.GET.get("date_max", "")
        if nom_form:
            liste = liste.filter(entrepreneur__nom__icontains=nom_form)
            form.fields['nom'].initial = nom_form
        if prenom_form:
            liste = liste.filter(entrepreneur__prenom__icontains=prenom_form)
            form.fields['prenom'].initial = prenom_form
        if date_min is not None and date_min != '':
            liste = liste.filter(date__gte=date_min)
            form.fields['date_min'].initial = date_min
        else:
            form.fields['date_min'].initial = ''
        if date_max is not None and date_max != '':
            liste = liste.filter(date__lte=date_max)
            form.fields['date_max'].initial = date_max
        else:
            form.fields['date_max'].initial = ''

    return render(request, "appflux/annuaire.html", locals())



def rendezvous_new(request):
    form = RendezVousAnnuaire()

    if request.method == 'POST':
        form = RendezVousAnnuaire(request.POST)
        if form.is_valid():
            rendezvous = form.save()
            subject = f"Nouveau rendez-vous avec {rendezvous.entrepreneur.nom}"
            message = f"Bonjour {rendezvous.entrepreneur.nom} {rendezvous.entrepreneur.prenom},\n\nVous avez un nouveau rendez-vous le {rendezvous.date} à {rendezvous.heure}\n\n. Le sujet du rendez-vous est : {rendezvous.sujet}\n\n Le mode d\'entretien du rendez-vous est : {rendezvous.lieu}\n\n La nature du rendez-vous est : {rendezvous.nature}\n\n Les objectifs du rendez vous sont : {rendezvous.objectifs}\n\n Cordialement ZECOOP"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [rendezvous.entrepreneur.email]
            send_mail(subject, message, from_email, recipient_list)
            
            return redirect('rendezvous')

    context = {
        'form': form,
    }

    return render(request, 'appflux/rendezvous_creer.html', context)

def rendezvous_detail_annuaire(request, rendezvous_id):
    rendezvous = get_object_or_404(RendezVous, id=rendezvous_id)

    context = {
        'rendezvous': rendezvous,
    }

    return render(request, 'appflux/rendezvousannuaire_detail.html', context)


def rendezvous_edit(request, rendezvous_id):
    rendezvous = get_object_or_404(RendezVous, id=rendezvous_id)
    form = RendezVousAnnuaire(instance=rendezvous)

    if request.method == 'POST':
        form = RendezVousAnnuaire(request.POST, instance=rendezvous)
        if form.is_valid():
            rendezvous = form.save()
            subject = f"Rendez-vous modifié avec {rendezvous.entrepreneur.nom}"
            message = f"Bonjour {rendezvous.entrepreneur.nom} {rendezvous.entrepreneur.prenom},\n\nVotre rendez-vous  a été modifié. Les nouvelles informations sont :\n\nNature : {rendezvous.nature}\nSujet : {rendezvous.sujet}\nObjectifs : {rendezvous.objectifs} \n\n\nLieu : {rendezvous.lieu}\nHeure : {rendezvous.heure}\nDate : {rendezvous.date}\n\nCordialement,\n ZECOOP"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [rendezvous.entrepreneur.email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('rendezvous')

    context = {
        'rendezvous': rendezvous,
        'form': form,
    }

    return render(request, 'appflux/rendezvous_formupdate.html', context)