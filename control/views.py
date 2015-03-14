from django.shortcuts import render
from .models import Sim , Venta
from django.views.generics import ListView


class SimListView(ListView):
	model = Sim
	template_name = 'sims.html'

class VentasListView(ListView):
	model = Venta
	template_name = 'venta.html'


