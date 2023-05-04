from django.db import models
from apps.core.models import BaseModel


class Cliente(BaseModel):
    nome = models.CharField('Nome', max_length=100)
    telefone = models.CharField('Telefone', max_length=30)

    def __str__(self):
        return self.nome
