from django.core.exceptions import ValidationError
import re
from django.utils.translation import ugettext as _


class ContainsDigitValidator:
    def validate(self, password, user=None):
        if not any(char.isdigit() for char in password):
            raise ValidationError(
                "Le mot de passe doit contenir un chiffre", code="password_no_digit"
            )

    def get_help_text(self):
        return "Votre mot de passe doit contenir au moins un chiffre !"
    
class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("Votre mot de passe ne contient pas de caractere speciale " ))


    def get_help_text(self):
        return _(
            ("Le mot de passe doit contenir un caractere speciale ")
        )