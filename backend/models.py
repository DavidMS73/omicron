from django.db import models


class Profesor(models.Model):
    nombre = models.CharField(max_length=60)
    correo = models.EmailField()
    celular = models.IntegerField()

class Estudiante(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=60)
    numCelular = models.IntegerField()
    numAcudiente = models.IntegerField()

class Cuaderno(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    trabajos = models.TextField(null=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    CLASIFICACIONES = [
        ('1', 'uno'),
        ('2', 'dos'),
    ]

    clasificacion = models.CharField(max_length=2, choices=CLASIFICACIONES, default='1')

class Materia(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    cantidad_estudiantes = models.IntegerField()
    bimestre = models.IntegerField()
    cuadernos = models.ManyToManyField(Cuaderno)

class Criterio(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=250)
    esCuantitativa = models.BooleanField(default=False)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    fechaInicio = models.DateTimeField(auto_now_add=True)
    fechaLimite = models.DateTimeField()

class Actividad(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    cuaderno = models.ForeignKey(Cuaderno, on_delete=models.CASCADE)
    criterio = models.ForeignKey(Criterio, on_delete=models.CASCADE)
    fechaEntrega = models.DateTimeField(auto_now_add=True)
    nota = models.DecimalField(max_digits=5, decimal_places=2)
    comentario = models.CharField(max_length=250)
    entregas = models.TextField(null=True)

class Tema(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250)
    recursos = models.CharField(max_length=500)