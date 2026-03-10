from django.db import models
from .Professor import Professor

class Disciplina(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    codigo = models.CharField(max_length=50)
    carga_horaria = models.IntegerField()
    descricao = models.TextField()
    professores = models.ManyToManyField(Professor, related_name='disciplinas')
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome