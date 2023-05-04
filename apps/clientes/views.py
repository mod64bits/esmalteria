from django.views.generic.list import ListView
from .models import Cliente


class ListaClienteView(ListView):
    model = Cliente
    template_name = "clientes/index.html"
