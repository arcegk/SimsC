from django.shortcuts import render
import json
from .models import Sim , Mes
from django.views.generic import ListView , CreateView , UpdateView ,View
from .forms import SimCreateViewForm , SimUpdateViewForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.core import serializers
from django.http import HttpResponse
from braces.views import LoginRequiredMixin , StaffuserRequiredMixin


class SimListViewtoUp(LoginRequiredMixin, ListView):

	model = Sim
	queryset = Sim.objects.all().order_by('fecha')
	template_name = 'sim_list.html'
	login_url = "/login"


	
class SimCreateView(StaffuserRequiredMixin, CreateView):
     model = Sim
     form_class = SimCreateViewForm
     template_name = "registrar.html"
     success_url = "/register"
     login_url = "/login"

class SimUpdateView(StaffuserRequiredMixin, UpdateView):
	model = Sim
	form_class = SimUpdateViewForm
	template_name = "sims_update.html"
	success_url = reverse_lazy('list_simstoUp')
	login_url = "/login"

class MesListView(ListView):
	model = Mes
	template_name = 'mes_list.html'
	
class ConsultaAjax(View):

	def get(self, request):
		pk = request.GET['id']
		obj = Sim.objects.all().exclude(meses__pk=pk)
		dic = []
		for o in obj:
			dic.append({'cliente' : o.cliente , 'numero' : o.numero, 'ide' : o.ide, } )
		return HttpResponse(json.dumps(dic) , content_type='application/json')
