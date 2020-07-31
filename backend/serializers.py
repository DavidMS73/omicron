from rest_framework import serializers

from .models import Profesor, Estudiante, Materia, Tema, Criterio, Cuaderno, Actividad, Entrega


class QRSerializer(serializers.Serializer):
    """
    This serializer is the output of create qr code
    """
    file_type = serializers.CharField(max_length=5)
    image_base64 = serializers.CharField(max_length=300)


class TemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tema
        fields = ('id', 'materia', 'nombre', 'descripcion', 'recursos')

class EntregaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrega
        fields = ('id', 'cuaderno', 'actividad', 'fechaEntrega',
                  'nota', 'comentario', 'archivos')

class ActividadSerializer(serializers.HyperlinkedModelSerializer):
    entregas = EntregaSerializer(many=True, required=False)
    class Meta:
        model = Actividad
        fields = ('id', 'materia', 'criterio', 'nombre', 'descripcion', 'fechaInicio',
                  'fechaLimite', 'qr', 'entregas')

class CriterioSerializer(serializers.HyperlinkedModelSerializer):
    actividades = ActividadSerializer(many=True, required=False)

    class Meta:
        model = Criterio
        fields = ('id', 'materia', 'nombre', 'descripcion', 'porcentaje',
         'actividades')

class CuadernoSerializer(serializers.HyperlinkedModelSerializer):
    entregas = EntregaSerializer(many=True, required=False)

    class Meta:
        model = Cuaderno
        fields = ('id', 'estudiante', 'materia',
                  'clasificacion', 'entregas')

class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    criterios = CriterioSerializer(many=True, required=False)
    actividades = ActividadSerializer(many=True, required=False)
    temas = TemaSerializer(many=True, required=False)
    cuadernos = CuadernoSerializer(many=True, required=False)

    class Meta:
        model = Materia
        fields = ('id', 'nombre', 'profesor', 'grado', 'bimestre', 'cantidad_estudiantes',
                'temas', 'criterios', 'actividades', 'cuadernos', 'color')

class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    cuadernos = CuadernoSerializer(many=True, required=False)

    class Meta:
        model = Estudiante
        fields = ('id', 'codigo', 'nombre', 'numCelular',
                  'numAcudiente', 'cuadernos')

class ProfesorSerializer(serializers.HyperlinkedModelSerializer):
    materias = MateriaSerializer(many=True, required=False)

    class Meta:
        model = Profesor
        fields = ('id', 'nombre', 'correo', 'celular', 'materias')
