from django.db import models

# Create your models here.
class Mes(models.Model):
	mes = models.CharField(max_length=50)

	def __str__(self):
		return self.mes		


class Sim(models.Model):

	ide = models.CharField(max_length=40 , unique=True)
	numero = models.CharField(max_length=15 ,null=True ,blank=True , unique=True)
	activa = models.BooleanField(default=False)
	valor = models.DecimalField(blank=True , default = 0 , max_digits=200 , decimal_places=1 )
	fecha = models.DateField(auto_now_add=True)
	cliente = models.CharField(max_length=50 , blank=True )
	meses = models.ManyToManyField(Mes , null = True)

	def __str__(self):
		return ("%s - %s") %(self.ide ,self.numero)

	def clean(self):
        
		if self.numero == "":
			self.numero = None
	def save(self , *args , **kwargs):
		if self.numero is not None:
			self.activa = True 
		super(Sim , self).save(*args , **kwargs)



