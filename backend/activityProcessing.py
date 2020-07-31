from .models import Profesor, Estudiante, Cuaderno, Actividad

# Varias funciones que se centran en tareas principales del sistema
def agregarActividades(celProf: str, codEst: str, entregas: str):
    try:
        profesor = Profesor.objects.get(celular=celProf)
        estudiante = Estudiante.objects.get(codigo=codEst)
        try:
            cuaderno = estudiante.cuadernos.get(clasificacion='1')
        except:
            cuaderno = estudiante.cuadernos.create(clasificacion='1')
        cuaderno.entregas.create(
            comentario='No se logró reconocer la actividad.', archivos=entregas)
    except Exception as e:
        print('################# Super F #################', str(e))