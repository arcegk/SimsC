from django.shortcuts import render
from .models import Sim , Venta
from django.views.generic import ListView


class SimListView(ListView):
	model = Sim
	template_name = 'sims.html'

class VentaListView(ListView):
	model = Venta
	template_name = 'venta.html'


