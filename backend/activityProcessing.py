from .models import Profesor, Estudiante, Cuaderno, Actividad
from .utils import get_act_from_image
from .fpdf.converter import crearDoc

# Varias funciones que se centran en tareas principales del sistema
def agregarActividades(celProf: str, codEst: str, entregas: str):
    try:
        profesor = Profesor.objects.get(celular=celProf)
        estudiante = Estudiante.objects.get(codigo=codEst)
        lista = entregas.split(';')
        for i in lista:
            try:
                act = get_act_from_image(i)
                actividad = Actividad.objects.get(id=act)
                materia = actividad.materia
                cuadernos_materia = estudiante.cuadernos.filter(materia_id=materia)
                if len(cuadernos_materia) == 1:
                    cuaderno = estudiante.cuadernos.get(materia=materia)
                elif len(cuadernos_materia) == 0:
                    cuaderno = estudiante.cuadernos.create(materia=materia)
                else:
                    cuaderno = estudiante.cuadernos.filter(materia_id=materia)[0]
                cuaderno.entregas.create(
                    comentario='Entrega hecha', actividad=actividad, archivos=i)
            except Exception as es:
                print(str(es))
                try:
                    cuaderno = estudiante.cuadernos.filter(materia__isnull=True)[0]
                except:
                    cuaderno = estudiante.cuadernos.create(clasificacion='1')
                cuaderno.entregas.create(
                    comentario='No se logró reconocer la actividad.', archivos=i)
    except Exception as e:
        print('################# Super F #################', str(e))

def getActivities(idEst, idMateria):
    cuadernos = Cuaderno.objects.filter(estudiante_id=idEst, materia_id=idMateria)
    if len(cuadernos) == 0:
        raise Exception('No hay cuadernos con los datos ingresados.')
    cuaderno = cuadernos[0]
    image_list = []
    for entrega in cuaderno.entregas.all():
        image_list.append(entrega.archivos)
    print('####### images: ', image_list)
    return crearDoc(image_list)