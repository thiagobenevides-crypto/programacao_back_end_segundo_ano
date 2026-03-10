from django.db import models
from .Aluno import Aluno
from .Disciplina import Disciplina
from .Professor import Professor

class Faltas(models.Model):
    STATUS_CHOICES = [('Presente', 'Presente'), ('Falta', 'Falta'), ('Atraso', 'Atraso'), ('Justificada', 'Justificada')]
    MOTIVO_CHOICES = [('Saúde', 'Saúde'), ('Transporte', 'Transporte'), ('Familiar', 'Familiar'), ('Outros', 'Outros')]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Presente')
    motivo = models.CharField(max_length=50, choices=MOTIVO_CHOICES, null=True, blank=True)
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)