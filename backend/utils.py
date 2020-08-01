from pyzbar.pyzbar import decode
from PIL import Image
import requests
import base64
import qrcode
import io

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
    generated_code.save(bio)
    png_qr = bio.getvalue()
    base64qr = base64.b64encode(png_qr)
    img_name = base64qr.decode("utf-8")
    context_dict = dict()
    context_dict['file_type'] = "png"
    context_dict['image_base64'] = img_name
    return context_dict

def get_act_from_image(url):
    response = requests.get(url)
    data = decode(Image.open(io.BytesIO(response.content)))
    try:
        text = data[0].data.decode('ascii')
    except:
        raise Exception('No se logró reconocer la actividad.')
    if not text.startswith('OMICRON:ACT'):
        raise Exception('No se logró reconocer la actividad.')
    return int(text[12:])