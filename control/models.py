from django.db import models

# Create your models here.
class Sim(models.Model):

	ide = models.CharField(max_length=40 , unique=True)
	numero = models.CharField(max_length=15 ,null=True ,blank=True , unique=True)
	activa = models.BooleanField(default=False)

	def __str__(self):
		return self.ide

	def clean(self):
        
		if self.numero == "":
			self.numero = None

class Venta(models.Model):

	fecha = models.DateField(auto_now=True)
	cliente = models.CharField(max_length=50)
	sim = models.ForeignKey(Sim)
	
	
	def __str__(self):
		return ("%s - %s - %s") %(self.fecha,self.cliente,self.sim.numero)
		

