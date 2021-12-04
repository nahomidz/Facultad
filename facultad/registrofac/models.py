from django.db import models

# Create your models here.
class registro(models.Model):
    matricula = models.CharField(max_length=9, blank=False)
    equipo = models.CharField(max_length=9, blank=False)
    comentario = models.TextField(max_length=100, blank=False)
    ipequipo = models.CharField(max_length=64,blank=False)
    salon = models.CharField(max_length=9, blank=False)
    def _str_(self):
        return '%s (%s - %s - %s)' % (self.matricula, self.equipo, self.ipequipo,self.salon)


