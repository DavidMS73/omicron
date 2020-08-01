from fpdf import FPDF
from os import remove
from urllib.request import urlretrieve
import requests, io

def crearDoc(image_list):
    pdf = FPDF()
    cont = 0
    for imagen in image_list:
        pdf.add_page()
        response = requests.get(imagen)
        open(str(cont)+".jpg", 'wb').write(response.content)
        #urlretrieve(imagen, str(cont)+".jpg")
        pdf.image(str(cont)+".jpg", 30, 15, 150)
        cont += 1
    pdf.output('tuto1.pdf', 'F')

    cont = 0
    
    for imagen in image_list:
        remove(str(cont)+".jpg")
        cont += 1
    
    return 'tuto1.pdf'