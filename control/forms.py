from django import forms
from .models import Venta, Sim , Mes

class VentaCreateViewForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(VentaCreateViewForm, self).__init__(*args, **kwargs)
		
		self.fields['meses'].widget= forms.CheckboxSelectMultiple()
		self.fields['meses'].queryset= Mes.objects.all()
		self.fields['meses'].help_text=""
			
	class Meta:
		model = Venta
		fields = ( 'cliente', 'sim' ,'meses' ,)


class VentaUpdateViewForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(VentaUpdateViewForm, self).__init__(*args, **kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.id:
			self.fields['meses'].widget= forms.CheckboxSelectMultiple()
			self.fields['meses'].queryset= Mes.objects.all()
			self.fields['meses'].help_text=""
			self.fields['sim'].widget.attrs['disabled'] = 'disabled'
			self.fields['sim'].required= False

	class Meta:
		model = Venta
		readonly_fields = ('sim' ,)
		fields = ( 'cliente', 'sim' ,'meses' ,)

	def clean_sim(self):
		instance = getattr(self, 'instance', None)
		if instance:
			return instance.sim
		else:
			return self.cleaned_data.get('sim', None)

class SimUpdateViewForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(SimUpdateViewForm, self).__init__(*args, **kwargs)
		self.fields['ide'].widget.attrs['readonly'] = True
				
	class Meta:
		model = Sim
		fields = '__all__'
