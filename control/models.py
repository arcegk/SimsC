from django.db import models

# Create your models here.
class Sim(models.Model):

	ide = models.CharField(max_length=40)
	numero = models.CharField(max_length=15)
	activa = models.BooleanField(default=False)

	def __str__(self):
		return self.ide

class Venta(models.Model):

	Fecha = models.DateField(auto_now=True)
	Vendedor = models.CharField(max_length=50)
	Sim = models.ForeignKey(Sim)

	def __str__(self):
		return ("%s - %s - %s") %(self.Fecha,self.Vendedor,self.Sim.numero)
		

