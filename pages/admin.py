from django.contrib import admin
from django.db import models
from django.db.models.base import Model
from .models import Categoria, Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'telefone', 'email', 'categoria']
    list_display_links = ['id', 'nome', 'email']
    list_editable = ['telefone']
    list_filter = ['nome']

admin.site.register(Categoria)
admin.site.register(Cliente, ClienteAdmin)