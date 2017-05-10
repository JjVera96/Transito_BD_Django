from django.db import models
from django.utils import timezone

class Multa(models.Model):
	placa_vehiculo = models.CharField(max_length = 6)
	documento_persona = models.CharField(max_length = 15)
	lugar = models.CharField(max_length = 40)
	fecha = models.DateField(default = timezone.now)
	observaciones = models.CharField(max_length = 255)

	def __unicode__(self):
		return "%s"%(str(self.id))