from django.contrib import admin 
from appflux.models import Entrepreneur
from django.contrib.auth.admin import UserAdmin

class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom', 'email')
    ordering = ('id',)
    search_fields = ('nom', 'prenom', 'email')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = () 


admin.site.register(Entrepreneur, EntrepreneurAdmin)

