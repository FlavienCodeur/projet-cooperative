from django.contrib import admin

from authentification.models import User
from django.contrib.auth.admin import UserAdmin


admin.site.register(User,UserAdmin)
