from django.shortcuts import render


def index(request):
    list_cliente = {
        'nome': 'Felipe',
        'idade': 28,
        'telefone': '48 99223 2323'
    }
    return render(request, 'clientes/index.html')