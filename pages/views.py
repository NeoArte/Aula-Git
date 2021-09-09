from django.shortcuts import redirect, render
from .models import Cliente
from .form import ClienteForm

# Create your views here.
def index(request):
    list_clientes = Cliente.objects.all()
    print(list_clientes)
    return render(request, "pages/index.html", {"clientes": list_clientes})

def details(request, pk):
    list_clientes = Cliente.objects.get(pk=pk)
    print(list_clientes)
    return render(request, 'pages/details.html')

def form(request):
    data = {}
    data['form'] = ClienteForm()
    return render(request, 'pages/form.html', data)

def create(request):
    form = ClienteForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')

def edit(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(instance=cliente)
    return render(request, 'pages/form.html', {'cliente': cliente, 'form': form})

def delete(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    cliente.delete()
    return redirect('index')

def update(request, pk):
    cliente = Cliente.objects.get(pk=pk)
    form = ClienteForm(request.POST, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('index')

def sobre(request):
    return render(request, "pages/sobre.html")


def servicos(request):
    return render(request, "pages/servicos.html")


def contatos(request):
    return render(request, "pages/contatos.html")
