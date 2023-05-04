from .models import Cliente
from django import forms
import datetime


class ClienteForm(forms.ModelForm):
    nome = forms.CharField(
        label="Cliente Nome",

    )

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Cliente
        fields = ("__all__")