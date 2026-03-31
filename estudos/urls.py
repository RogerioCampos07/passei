from django.urls import path
from . import views

# O app_name ajuda a organizar os links nos templates (Namespacing)
app_name = 'estudos'

urlpatterns = [
    # Página inicial da app (Lista de Cursos)
    path('', views.CursoListView.as_view(), name='lista_cursos'),
    
    # Detalhe de um curso específico
    path('curso/<int:pk>/', views.CursoDetailView.as_view(), name='detalhe_curso'),
    
    # Rota para processar a adição de horas (POST)
    path('topico/<int:pk>/estudar/', views.RegistrarEstudoView.as_view(), name='registrar_estudo'),
]