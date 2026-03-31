from django.contrib import admin
from .models import Curso, Materia, Topico

# 1. Configuração para criar Tópicos dentro da Matéria (Inline)
class TopicoInline(admin.TabularInline):
    model = Topico
    extra = 1  # Quantidade de linhas em branco para novos tópicos
    fields = ('nome', 'tempo_estudado')

# 2. Personalização da Matéria
@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'meta_recompensa_horas', 'get_tempo_total')
    search_fields = ('nome',)
    inlines = [TopicoInline] # Permite criar tópicos na mesma tela!

    def get_tempo_total(self, obj):
        # Chama a property que criamos no models.py
        return obj.tempo_total_materia
    get_tempo_total.short_description = 'Total Estudado'

# 3. Personalização do Curso
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)
    # Filtro lateral para facilitar a busca
    list_filter = ('nome',)
    # Melhor interface para selecionar matérias (Many-to-Many)
    filter_horizontal = ('materias',)

# 4. Personalização do Tópico (Caso queira editar isolado)
@admin.register(Topico)
class TopicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'materia', 'tempo_estudado')
    list_filter = ('materia',)
    search_fields = ('nome',)