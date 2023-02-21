from django.contrib import admin 
from appflux.models import Entrepreneur, Fichier
from django.contrib.auth.admin import UserAdmin

class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'email')
    ordering = ('id',)
    search_fields = ('nom', 'prenom', 'email')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = () 


admin.site.register(Entrepreneur, EntrepreneurAdmin)

class FichierAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom',)
    ordering = ('id',)
    search_fields = ('nom', 'entrepreneur',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = () 

admin.site.register(Fichier, FichierAdmin)
