from django.db import models
from .Turma import Turma
from .Disciplina import Disciplina

class CalendarioEscolar(models.Model):
    TIPO_CHOICES = [('Letivo', 'Letivo'), ('Feriado', 'Feriado'), ('Recesso', 'Recesso')]
    
    data = models.DateField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='Letivo')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, null=True, blank=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.data} - {self.tipo}"