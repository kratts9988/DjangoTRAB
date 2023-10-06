"""
URL configuration for projeto_estoque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importa a classe `admin` do módulo `django.contrib`
from django.contrib import admin

# Importa a função `path` e o módulo `include` do módulo `django.urls`
from django.urls import path, include

# Importa as views do aplicativo `estoque`
from estoque import views


# Lista de URLs
urlpatterns = [
    # Define a rota para o painel de administração do Django
    path("admin/", admin.site.urls),
    
    # Define uma rota para a criação de um novo item
    path("novo_item/", views.novo_item, name="novo_item"),
    
    # Define uma rota para a adição de um novo item
    path("adicionar/", views.adicionar_item, name="adicionar_item"),
    
    # Define a rota padrão, que lista os itens em estoque
    path("", views.lista_estoque),
    
    # Define uma rota para listar os itens em estoque
    path("lista_estoque/", views.lista_estoque, name="lista_estoque"),
    
    # Define uma rota para os detalhes de um item
    path("<int:id>/", views.detalhes_item, name="detalhes_item"),
    
    # Define uma rota para editar um item
    path("<int:id>/editar/", views.editar_item, name="editar_item"),
    
    # Define uma rota para confirmar a exclusão de um item
    path("<int:id>/excluir/",views.confirmar_exclusao_item, name="confirmar_exclusao_item"),
    
    # Define uma rota para efetuar a exclusão de um item
    path('<int:id>/excluir/confirmar/', views.excluir_item, name='excluir_item'),
]