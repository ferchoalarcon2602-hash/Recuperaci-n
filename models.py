

# Create your models here.
from django.db import models

# Create your models here.
class aprendiz (models.Model):
    nombre  = models.CharField(max_length = 25)
    apellido = models.CharField(max_length = 25)
    documento = models.IntegerField(unique = True)
    correo = models.EmailField(unique = True)
    telefono = models.IntegerField(unique=True)
    ficha = models.IntegerField()
    tipo_de_documento = models.CharField(max_length = 25)





    def __str__ (self):
        return f'{self.nombre.apellido.documento.correo.telefono.ficha.tipo_de_documento}'

from django.db import models
class programa (models.Model):
    nombre  = models.CharField(max_length = 30)
    ficha = models.IntegerField()
    jornada = models.CharField(max_length = 15)
    lugar = models.CharField(max_length = 20)
    duracion = models.CharField(max_length = 30)
    modalidad = models.CharField(max_length = 15)
    nivel_de_profecion = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 100)

    def __str__ (self):
        return f'{self.nombre.ficha.jornada.lugar.duracion.modalidad.nivel_de_profecion.descripcion}'

from django.db import models
class instructor (models.Model):
    nombre  = models.CharField(max_length = 25)
    apellido = models.CharField(max_length = 25)
    especialidad  = models.CharField(max_length = 25)
    documento = models.IntegerField(unique = True)
    ficha_asignada = models.IntegerField()
    correo = models.EmailField(unique = True)
    telefono = models.IntegerField(unique=True)

    def __str__ (self):
        return f'{self.nombre.apellido.especialidad.documento.ficha_asignada.correo.telefono}'





from django.db import models
class competencias (models.Model):
     nombre  = models.CharField(max_length = 30)
     ficha = models.IntegerField()
     instructor = models.CharField(max_length = 30)

     def __str__ (self):
        return f'{self.nombre.ficha.instructor}'


    
    