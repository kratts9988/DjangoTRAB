# Importa as funções e classes necessárias do Django
from django.shortcuts import render, redirect, get_object_or_404

# Importa o modelo ItemEstoque da sua aplicação
from .models import ItemEstoque

# Importa os formulários definidos em forms.py
from .forms import NovoItemForm, ItemEstoqueForm


def lista_estoque(request):
    """
    Renderiza a lista de itens em estoque.

    Retorna um template HTML com a lista de itens e um link para adicionar um novo item.

    Args:
        request: A requisição HTTP.

    Returns:
        Um objeto HttpResponse com o conteúdo da página.

    """
    itens = ItemEstoque.objects.all()  # Obtém todos os itens do estoque
    return render(request, "estoque/lista_estoque.html", {"itens": itens})


def novo_item(request):
    """
    Cria um novo item no estoque.

    Se o método da requisição for POST e o formulário for válido, o novo item é criado e o usuário é redirecionado para a
    lista de itens.

    Args:
        request: A requisição HTTP.

    Returns:
        Um objeto HttpResponse com o conteúdo da página.

    """
    if request.method == "POST":
        form = NovoItemForm(request.POST)  # Cria um formulário com os dados da requisição POST
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva o novo item no banco de dados
            return redirect("lista_estoque")  # Redireciona para a lista de itens
    else:
        form = NovoItemForm()  # Cria um formulário vazio (para ser preenchido pelo usuário)

    return render(request, "estoque/novo_item.html", {"form": form})


def adicionar_item(request):
    """
    Adiciona um novo item ao estoque.

    Se o método da requisição for POST e o formulário for válido, o novo item é criado e o usuário é redirecionado para a
    lista de itens.

    Args:
        request: A requisição HTTP.

    Returns:
        Um objeto HttpResponse com o conteúdo da página.

    """
    if request.method == "POST":
        form = NovoItemForm(request.POST)  # Cria um formulário com os dados da requisição POST
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva o novo item no banco de dados
            return redirect("lista_estoque")  # Redireciona para a lista de itens
    else:
        form = NovoItemForm()  # Cria um formulário vazio (para ser preenchido pelo usuário)

    return render(request, "estoque/adicionar_item.html", {"form": form})


def detalhes_item(request, id):
    """
    Mostra os detalhes de um item do estoque.

    Args:
        request: A requisição HTTP.
        id: O ID do item.

    Returns:
        Um objeto HttpResponse com o conteúdo da página.

    """
    item = get_object_or_404(ItemEstoque, id=id)  # Obtém o item com o ID fornecido
    return render(request, "estoque/detalhes_item.html", {"item": item})


def editar_item(request, id):
    """
    Edita um item do estoque.

    Se o método da requisição for POST e o formulário for válido, as alterações são salvas e o usuário é redirecionado
    para a página de detalhes do item.

    Args:
        request: A requisição HTTP.
        id: O ID do item.

    Returns:
        Um objeto HttpResponse com o conteúdo da página.

    """
    item = get_object_or_404(ItemEstoque, id=id)  # Obtém o item com o ID fornecido

    if request.method == "POST":
        form = ItemEstoqueForm(request.POST, instance=item)  # Cria um formulário com os dados da requisição POST
        if form.is_valid():  # Verifica se o formulário é válido
            form.save()  # Salva as alterações no item
            return redirect("detalhes_item", id=id)  # Redireciona para a página de detalhes do item
    else:
        form = ItemEstoqueForm(instance=item)  # Cria um formulário preenchido com os dados atuais do item

    return render(request, "estoque/editar_item.html", {"form": form, "item": item})


def confirmar_exclusao_item(request, id):
    """
    Página de confirmação de exclusão de um item.

    Args:
        request: A requisição HTTP.
        id: O ID do item.

    Returns:
        Um objeto HttpResponse com o conteúdo da página.

    """
    item = get_object_or_404(ItemEstoque, id=id)  # Obtém o item com o ID fornecido
    return render(request, "estoque/confirmar_exclusao_item.html", {"item": item})


def excluir_item(request, id):
    """
    Exclui um item do estoque.

    Após a exclusão, o usuário é redirecionado para a lista de itens.

    Args:
        request: A requisição HTTP.
        id: O ID do item.

    Returns:
        Um objeto HttpResponse com o conteúdo da página.

    """
    item = get_object_or_404(ItemEstoque, id=id)  # Obtém o item com o ID fornecido
    item.delete()  # Exclui o item do banco de dados
    return redirect("lista_estoque")  # Redireciona para a lista de itens