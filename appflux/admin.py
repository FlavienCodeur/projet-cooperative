from django.contrib import admin 
from appflux.models import Entrepreneur
from django.contrib.auth.admin import UserAdmin

class EntrepreneurAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prenom')
    ordering = ('id',)


admin.site.register(Entrepreneur, EntrepreneurAdmin)

