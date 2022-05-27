from django.db import models

# Create your models here.
class Cliente(models.Model):
    Nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.IntegerField(max_length=100)
    endereco = models.CharField(max_length=100)
    profissao = models.CharField(max_length=100)