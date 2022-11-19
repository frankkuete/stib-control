from django import forms
from stibapp.models import User, Admin, Station, Line, StationOrder, Control
from django.utils.translation import gettext_lazy as _


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'pseudo': _('Entrer votre pseudo'),
            'password': _('Entrer votre mot de passe'),
            'isadmin': _('Voulez vous etre un administrateur ?'),
        }


class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ['code']
        labels = {
            'code': _('Entrer votre code secret'),
        }


class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = '__all__'
        labels = {
            'station_name': _('Entrer le nom de la station '),
            'locality': _('Entrer le nom de la commune ou se trouve la station'),
        }


class LineForm(forms.ModelForm):
    class Meta:
        model = Line
        fields = '__all__'
        labels = {
            'direction': _('Entrer la direction ( le nom du terminus ) '),
            'category': _('Choissisez le type de ligne (TRAM ? BUS ? ou METRO ?)  '),
            'number': _('Selectionner le numero de la ligne ')
        }


class StationOrderForm(forms.ModelForm):
    class Meta:
        model = StationOrder
        fields = '__all__'
        labels = {
            'line': _('Entrer la direction ( le nom du terminus ) '),
            'station': _('Choisissez la station présente dans cette ligne '),
            'order': _("Selectionner l'ordre de la station dans la ligne")
        }

class ControlForm(forms.ModelForm):
    class Meta:
        model = Control
        fields = '__all__'
        labels = {
            'Station': _('Entrer la station est effectué le controle '),
            'Line': _('Choisissez la ligne concernée par le controle  ')
        }