from rest_framework import viewsets
from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status, APIView
from .serializers import ProfesorSerializer, ActividadSerializer, CriterioSerializer, CuadernoSerializer, EstudianteSerializer, MateriaSerializer, TemaSerializer, QRSerializer
from .models import Profesor, Actividad, Criterio, Cuaderno, Estudiante, Materia, Tema
from .utils import generate_qr
from .decorators import validate_request_data
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from django.http import HttpResponse, HttpResponseBadRequest
from django.views import View
import json
import backend.utils as ut
from django.views.decorators.csrf import csrf_exempt
from .fpdf.converter import *
from django.utils.decorators import method_decorator


# Create your views here.


class CreateQRView(generics.CreateAPIView):
    """
    POST create/
    """
    permission_classes = (permissions.AllowAny,)
    queryset = ''
    serializer_class = QRSerializer
    throttle_classes = [AnonRateThrottle]

    @validate_request_data
    def post(self, request, *args, **kwargs):
        text = request.data['text']
        output = generate_qr(text)
        result = QRSerializer(output).data
        return Response(
            data=result,
            status=status.HTTP_201_CREATED
        )


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
