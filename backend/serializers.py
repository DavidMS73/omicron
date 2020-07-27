from rest_framework import serializers

from .models import Profesor, Estudiante, Materia, Tema, Criterio, Cuaderno, Actividad

class ProfesorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profesor
        fields = ('nombre', 'correo', 'celular')

class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estudiante
        fields = ('id', 'nombre', 'numCelular', 'numAcudiente')

class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Materia
        fields = ('profesor', 'nombre', 'cantidad_estudiantes', 'bimestre', 'cuadernos')

class TemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tema
        fields = ('materia', 'nombre', 'descripcion', 'recursos')

class CriterioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Criterio
        fields = ('nombre', 'descripcion', 'esCuantitativa', 'porcentaje', 'fechaInicio', 'fechaLimite')

class ActividadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actividad
        fields = ('id', 'cuaderno', 'criterio', 'fechaEntrega', 'nota', 'comentario', 'entregas')

class CuadernoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuaderno
        fields = ('id', 'trabajos', 'estudiante', 'clasificacion')