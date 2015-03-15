from django.shortcuts import render
import json
from .models import Sim , Venta , Mes
from django.views.generic import ListView , CreateView , UpdateView ,View
from .forms import VentaCreateViewForm , VentaUpdateViewForm , SimUpdateViewForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.core import serializers
from django.http import HttpResponse


class SimListViewtoUp(ListView):

	model = Sim
	template_name = 'sim_list.html'

class VentaListView(ListView):

	model = Venta
	template_name = 'venta.html'

	
class VentaCreateView(CreateView):
     model = Venta
     form_class = VentaCreateViewForm
     template_name = "registrar.html"
     success_url = "/register"

class SimUpdateView(UpdateView):
	model = Sim
	form_class = SimUpdateViewForm
	template_name = "sims_update.html"
	success_url = reverse_lazy('list_simstoUp')

class VentaUpdateView(UpdateView):
	model = Venta
	form_class = VentaUpdateViewForm
	template_name = "venta_update.html"
	success_url = reverse_lazy('list_ventas')

class MesListView(ListView):
	model = Mes
	template_name = 'mes_list.html'
	
class ConsultaAjax(View):

	def get(self, request):
		pk = request.GET['id']
		obj = Venta.objects.filter(meses__pk=pk)
		print obj
		data = serializers.serialize('json' , obj , fields={'cliente' , 'sim.numero' , 'sim.ide'})
		return HttpResponse(data , content_type='application/json')
