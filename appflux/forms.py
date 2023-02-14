from django.forms import ModelForm, Form , CharField
from appflux.models import Entrepreneur

class EntrepreneurForm(ModelForm):
    class Meta:
       model = Entrepreneur
       fields = '__all__'


class EntrepreneurFiltre(Form):
    nom = CharField(max_length=100, required=False)
    prenom = CharField(max_length=100, required=False)
    structure = CharField(max_length=100, required=False)
