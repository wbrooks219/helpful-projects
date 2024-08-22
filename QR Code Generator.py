# This is a Program that generates QR codes
import qrcode
import shutil
import os
from pathlib import Path


url = input("Please enter the text you want in a qrcode:")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
)

qr.add_data(url)

qr.make(fit = True)

img = qr.make_image(fill_color="black", back_color="white")

filename = input("Please enter QR code name:") + ".png"

img.save(filename)

downloadspath = str(Path.home() / "Downloads")

currentpath = os.getcwd() + "/" + filename

shutil.move(currentpath, downloadspath)
