from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from proyecto.models import Clientes, Articulos, Pedidos, Comunicado, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse
from django.template import Template, Context
# Create your views here.
