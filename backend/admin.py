from django.contrib import admin
from .models import Profesor, Estudiante, Cuaderno, Materia, Actividad, Criterio, Tema

# Register your models here.
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Cuaderno)
admin.site.register(Actividad)
admin.site.register(Criterio)
admin.site.register(Materia)
admin.site.register(Tema)
