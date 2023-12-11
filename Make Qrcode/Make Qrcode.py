# pip install qrcode

import os
import qrcode
a = input("your link : ")
img = qrcode.make(a)
img.save("qr.png", "PNG")
os.system("open qr.png")