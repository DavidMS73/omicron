from fpdf import FPDF
from os import remove
from urllib.request import urlretrieve

def crearDoc():
    image_list = ["https://s3-external-1.amazonaws.com/media.twiliocdn.com/AC1153435c9e58cbfcd3a06b9305b81187/5b8f4b4fb53ab4568a7f39e45d8c8213", "https://s3-external-1.amazonaws.com/media.twiliocdn.com/AC1153435c9e58cbfcd3a06b9305b81187/5b8f4b4fb53ab4568a7f39e45d8c8213"]
    pdf = FPDF()
    cont = 0
    for imagen in image_list:
        pdf.add_page()
        urlretrieve(imagen, str(cont)+".jpg")
        pdf.image(str(cont)+".jpg", 30, 15, 150)
        cont += 1
    pdf.output('tuto1.pdf', 'F')

    cont = 0
    
    for imagen in image_list:
        remove(str(cont)+".jpg")
        cont += 1