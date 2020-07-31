# #################################
# Generate QR code
import pyqrcode


def generateQrMessage(stringToEncode, idImgQr):
    qr = pyqrcode.create(stringToEncode)
    qr.png(idImgQr+".png", scale=8)
