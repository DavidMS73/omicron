from rest_framework import serializers

from .models import Profesor, Estudiante, Materia, Tema, Criterio, Cuaderno, Actividad


class QRSerializer(serializers.Serializer):
    """
    This serializer is the output of create qr code
    """
    file_type = serializers.CharField(max_length=5)
    image_base64 = serializers.CharField(max_length=300)


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
        fields = ('profesor', 'nombre', 'cantidad_estudiantes',
                  'bimestre', 'grado', 'color', 'cuadernos')


class TemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tema
        fields = ('materia', 'nombre', 'descripcion', 'recursos')


class CriterioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Criterio
        fields = ('nombre', 'descripcion', 'esCuantitativa',
                  'porcentaje', 'fechaInicio', 'fechaLimite')


class ActividadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actividad
        fields = ('id', 'cuaderno', 'criterio', 'fechaEntrega',
                  'nota', 'comentario', 'entregas')


class CuadernoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuaderno
        fields = ('id', 'trabajos', 'estudiante', 'clasificacion')
