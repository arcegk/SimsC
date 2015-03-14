from django.shortcuts import render
from .models import Sim , Venta
from django.views.generic import ListView , CreateView


class SimListView(ListView):
	model = Sim
	template_name = 'sims.html'

class VentaListView(ListView):
	model = Venta
	template_name = 'venta.html'


class VentaCreateView(CreateView):
     model = Venta
     template_name = "registrar.html"
     success_url = "/register"