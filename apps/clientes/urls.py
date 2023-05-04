from django.urls import path
from .views import ListaClienteView

app_name = 'clientes'

urlpatterns = [

    path('', ListaClienteView.as_view(), name='lista_clientes'),

]