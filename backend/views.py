from rest_framework import viewsets
from .serializers import ProfesorSerializer, ActividadSerializer, CriterioSerializer, CuadernoSerializer, EstudianteSerializer, MateriaSerializer, TemaSerializer
from .models import Profesor, Actividad, Criterio, Cuaderno, Estudiante, Materia, Tema

# Create your views here.

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer

class TemaViewSet(viewsets.ModelViewSet):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializer

class CriterioViewSet(viewsets.ModelViewSet):
    queryset = Criterio.objects.all()
    serializer_class = CriterioSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class CuadernoViewSet(viewsets.ModelViewSet):
    queryset = Cuaderno.objects.all()
    serializer_class = CuadernoSerializer