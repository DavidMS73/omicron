from rest_framework import serializers

from .models import Profesor, Estudiante, Materia, Tema, Criterio, Cuaderno, Actividad

class TemaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tema    
        fields = ('id', 'materia', 'nombre', 'descripcion', 'recursos')

class ActividadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actividad
        fields = ('id', 'cuaderno', 'criterio', 'fechaEntrega', 'nota', 'comentario', 'entregas')

class CriterioSerializer(serializers.HyperlinkedModelSerializer):
    actividades = ActividadSerializer(many=True, required=False)
    class Meta:
        model = Criterio
        fields = ('id', 'materia', 'nombre', 'descripcion', 'esCuantitativa', 'porcentaje', 'fechaInicio', 'fechaLimite', 'actividades')

class CuadernoSerializer(serializers.HyperlinkedModelSerializer):
    actividades = ActividadSerializer(many=True)
    class Meta:
        model = Cuaderno
        fields = ('id', 'trabajos', 'estudiante', 'clasificacion', 'materia', 'actividades')

class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    cuadernos = CuadernoSerializer(many=True, read_only=True)
    class Meta:
        model = Estudiante
        fields = ('id', 'codigo', 'nombre', 'numCelular', 'numAcudiente', 'cuadernos')

class MateriaSerializer(serializers.HyperlinkedModelSerializer):
    cuadernos = CuadernoSerializer(many=True, read_only=True)
    criterios = CriterioSerializer(many=True)
    temas = TemaSerializer(many=True)
    class Meta:
        model = Materia
        fields = ('id', 'profesor', 'nombre', 'cantidad_estudiantes', 'bimestre', 'cuadernos', 'criterios', 'temas')

class ProfesorSerializer(serializers.HyperlinkedModelSerializer):
    materias = MateriaSerializer(many=True, read_only=True)
    class Meta:
        model = Profesor
        fields = ('id', 'nombre', 'correo', 'celular', 'materias')