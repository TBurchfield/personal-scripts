#!/usr/bin/env python3
import requests
import threading
import binascii
from PIL import Image

def requestsget(s):
  requests.get(s)

im = Image.open("windows.png")
pix = im.load()

i = 0
for col in range(im.size[1]):
  for row in range(im.size[0]):
    if i % 2 == 0:
      s = '%02x%02x%02x' % (pix[row, col][0:3])
      x = threading.Thread(target=requestsget, args=['http://gradcap.us/write?id=cell_{}&color=%23{}'.format(i, s)])
      x.start()
    i+=1
