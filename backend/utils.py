import base64
import qrcode
import io
from .models import Profesor, Estudiante, Cuaderno, Actividad


def generate_qr_code(data, size=10, border=0):
    qr = qrcode.QRCode(
        version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=size, border=border)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image()
    return img


def generate_qr(url_text):
    generated_code = generate_qr_code(data=url_text, size=10, border=1)
    bio = io.BytesIO()
    img_save = generated_code.save(bio)
    png_qr = bio.getvalue()
    base64qr = base64.b64encode(png_qr)
    img_name = base64qr.decode("utf-8")
    context_dict = dict()
    context_dict['file_type'] = "png"
    context_dict['image_base64'] = img_name
    return context_dict


# Varias funciones que se centran en tareas principales del sistema
def agregarActividades(celProf: str, codEst: str, entregas: str):
    try:
        profesor = Profesor.objects.get(celular=celProf)
        estudiante = Estudiante.objects.get(codigo=codEst)
        try:
            cuaderno = estudiante.cuadernos.get(clasificacion='1')
        except:
            cuaderno = estudiante.cuadernos.create(clasificacion='1')
        cuaderno.actividades.create(
            comentario='No se logró reconocer la actividad.', entregas=entregas)
    except Exception as e:
        print('################# Super F #################', str(e))
