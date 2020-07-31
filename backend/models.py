from django.db import models
import json
from .utils import generate_qr

class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    celular = models.CharField(max_length=15)

class Estudiante(models.Model):
    codigo = models.CharField(max_length=10, default='0')
    nombre = models.CharField(max_length=60)
    numCelular = models.CharField(max_length=15)
    numAcudiente = models.CharField(max_length=15)

class Materia(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=60)
    cantidad_estudiantes = models.IntegerField()
    bimestre = models.IntegerField()
    grado = models.CharField(max_length=10, default='0')
    color = models.CharField(max_length=10, default='1')

class Cuaderno(models.Model):
    estudiante = models.ForeignKey(Estudiante, related_name='cuadernos', on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, related_name='cuadernos', on_delete=models.CASCADE, null=True)

    CLASIFICACIONES = [
        ('1', 'uno'),
        ('2', 'dos'),
    ]

    clasificacion = models.CharField(
        max_length=2, choices=CLASIFICACIONES, default='1')

class Criterio(models.Model):
    materia = models.ForeignKey(Materia, related_name='criterios', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=250)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)

class Actividad(models.Model):
    materia = models.ForeignKey(Materia, related_name='actividades', null=True, on_delete=models.CASCADE)
    criterio = models.ForeignKey(Criterio, related_name='actividades', null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=250)
    fechaInicio = models.DateTimeField(auto_now_add=True)
    fechaLimite = models.DateTimeField()
    qr = models.CharField(max_length=1000, default='NOJSON')

    def save(self, *args, **kwargs):
        add = not self.pk
        super(Actividad, self).save(*args, **kwargs)
        if add:
            self.qr = json.dumps(generate_qr('OMICRON:ACT:'+str(self.id)))
            kwargs['force_insert'] = False # create() uses this, which causes error.
            super(Actividad, self).save(*args, **kwargs)

class Entrega(models.Model):
    cuaderno = models.ForeignKey(Cuaderno, related_name='entregas', on_delete=models.CASCADE)
    actividad = models.ForeignKey(Actividad, related_name='entregas', null=True, on_delete=models.CASCADE)
    fechaEntrega = models.DateTimeField(auto_now_add=True)
    nota = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    comentario = models.CharField(max_length=250, null=True)
    archivos = models.TextField(null=True)

class Tema(models.Model):
    materia = models.ForeignKey(Materia, related_name='temas', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    recursos = models.CharField(max_length=500)
