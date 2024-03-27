# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:14:58 2023

@author: HADES
"""

import qrcode

def generate_qr(text,img_name):
    qr= qrcode.QRCode(
        version =1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    #saving image as png to makeit more accessible
    img.save(img_name + ".png")
print("HEllo there!!")
a=input("Enter the link you want the qr code to be generated for XD:: ")
img_name=input("Enter image name, ")    
print("MAKING THE QR...")
#sending 2 variables to the generator function 1 being the text to be converted to qr , other being the image name
generate_qr(a,img_name)
print("ITS DONEE!!!!, GO CHECK IT OUT")    
    