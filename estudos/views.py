from django.views.generic import ListView, DetailView, View
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Curso, Topico, Materia
from datetime import timedelta

class CursoListView(ListView):
    model = Curso
    template_name = 'estudos/lista_cursos.html'
    context_object_name = 'cursos'

class CursoDetailView(DetailView):
    model = Curso
    template_name = 'estudos/lista_cursos.html'

class MateriaDetailView(DetailView):
    model = Materia
    template_name = 'estudos/detalhe_materia.html'

class TopicoDetailView(DetailView):
    model = Topico
    template_name = 'estudos/detalhe_topico.html'
    

class RegistrarEstudoView(View):
    """View para adicionar tempo a um tópico via POST"""
    def post(self, request, pk):
        topico = get_object_or_404(Topico, pk=pk)
        minutos = int(request.POST.get('minutos', 0))
        
        # Atualiza o tempo usando timedelta
        topico.tempo_estudado += timedelta(minutes=minutos)
        topico.save()
        
        # Verifica a recompensa (Lógica simples para exemplo)
        materia = topico.materia
        if materia.tempo_total_materia.total_seconds() >= (materia.meta_recompensa_horas * 3600):
            messages.success(request, f"🏆 VAI CORINTHIANS! Você desbloqueou a recompensa em {materia.nome}!")
        
        return redirect('estudos:detalhe_curso', pk=topico.materia.cursos_vinculados.first().pk)