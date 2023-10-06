from django import forms  # Importa as classes de formulário do Django
from .models import ItemEstoque  # Importa o modelo ItemEstoque do aplicativo atual

class NovoItemForm(forms.ModelForm):
    class Meta:
        model = ItemEstoque  # Define o modelo associado a este formulário
        fields = ['nome', 'descricao', 'quantidade']  # Define quais campos do modelo serão exibidos no formulário

class ItemEstoqueForm(forms.ModelForm):
    class Meta:
        model = ItemEstoque  # Define o modelo associado a este formulário
        fields = ['nome', 'descricao', 'quantidade']  # Define quais campos do modelo serão exibidos no formulário