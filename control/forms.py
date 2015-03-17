from django import forms
from .models import Sim , Mes

class SimCreateViewForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(SimCreateViewForm, self).__init__(*args, **kwargs)
		
		self.fields['meses'].widget= forms.CheckboxSelectMultiple()
		self.fields['meses'].queryset= Mes.objects.all()
		self.fields['meses'].help_text=""
			
	class Meta:
		model = Sim
		fields = '__all__'



class SimUpdateViewForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(SimUpdateViewForm, self).__init__(*args, **kwargs)
		self.fields['ide'].widget.attrs['readonly'] = True
		self.fields['meses'].widget= forms.CheckboxSelectMultiple()
		self.fields['meses'].queryset= Mes.objects.all()
		self.fields['meses'].help_text=""
				
	class Meta:
		model = Sim
		fields = '__all__'
