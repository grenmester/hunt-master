import PIL
import qrcode

def make_qr(path,s):
    """
    Returns a QR Code image that generates the text in s
    """
    img = qrcode.make(s)
    img.save(path)
