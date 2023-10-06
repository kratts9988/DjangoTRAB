from django.db import models

class ItemEstoque(models.Model):
    # Define um campo de texto para o nome do item com no máximo 100 caracteres
    nome = models.CharField(max_length=100)
    
    # Define um campo de texto para a descrição do item (pode ser mais longa)
    descricao = models.TextField()
    
    # Define um campo para a quantidade do item, com valor padrão de 0
    quantidade = models.PositiveIntegerField(default=0) 

    # Define como o item é representado quando convertido para string
    def __str__(self):
        return self.nome