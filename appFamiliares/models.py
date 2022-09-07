from django.db import models

class Familiares(models.Model):
    nombre = models.CharField(max_length=60)
    calle = models.CharField(max_length=60)
    altura = models.IntegerField()
    fechaNac = models.DateField()
    
    def __str__ (self):
        return self.nombre
    
    
