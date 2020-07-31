from rest_framework import viewsets
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
import json
import backend.utils as ut
from django.views.decorators.csrf import csrf_exempt
from .serializers import ProfesorSerializer, ActividadSerializer, CriterioSerializer, CuadernoSerializer, EstudianteSerializer, MateriaSerializer, TemaSerializer
from .models import Profesor, Actividad, Criterio, Cuaderno, Estudiante, Materia, Tema
from .fpdf.converter import *
from django.utils.decorators import method_decorator
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

@method_decorator(csrf_exempt, name='dispatch')
class ActividadSubmitView(View):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body)
        if 'codEst' in data and 'celProf' in data:
            codEst = data['codEst']
            celProf = data['celProf']
            entregas = data['entregas']
            ut.agregarActividades(celProf, codEst, entregas)
            return HttpResponse()
        else:
            return HttpResponseBadRequest()

class CreatePDF(viewsets.ViewSet):
    crearDoc()
