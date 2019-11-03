from django.db import models

class TD_Categoria(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField()
