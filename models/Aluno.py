from django.db import models
from .Turma import Turma

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='alunos')
    email = models.EmailField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome