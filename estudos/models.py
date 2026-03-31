from django.db import models
from datetime import timedelta

class Curso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField(blank=True)
    # O segredo: ManyToManyField permite selecionar múltiplas matérias existentes
    materias = models.ManyToManyField('Materia', related_name='cursos_vinculados', blank=True)

    def __str__(self):
        return self.nome

class Materia(models.Model):
    nome = models.CharField(max_length=100) # Ex: Python, Django, Linux
    meta_recompensa_horas = models.PositiveIntegerField(default=100)

    @property
    def tempo_total_materia(self):
        # Soma o tempo de todos os tópicos vinculados a esta matéria
        total = sum([t.tempo_estudado for t in self.topicos.all()], timedelta())
        return total

    def __str__(self):
        return self.nome

# O Topico continua ligado à Materia
class Topico(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, related_name='topicos')
    nome = models.CharField(max_length=100)
    tempo_estudado = models.DurationField(default=timedelta(0))

    def __str__(self):
        return f"{self.nome} ({self.materia.nome})"