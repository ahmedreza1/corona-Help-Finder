from django.db import models

# Create your models here.
class State(models.Model):
	state = models.CharField(max_length=500)
	created = models.DateTimeField(auto_now=True)

	def __str__(self):
		return '{}'.format(self.state)

	class Meta:
		verbose_name_plural = 'states'