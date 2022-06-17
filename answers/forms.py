from .models import Uset
from django.forms import ModelForm


class UsetForm(ModelForm):
    class Meta:
        model = Uset
        fields = ['born_date']
