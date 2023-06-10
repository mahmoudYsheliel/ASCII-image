

import numpy as np
import cv2
import imutils
from  scipy import signal
import time
import os



img = cv2.imread("wan.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


resized = imutils.resize(img_gray, width=175)
result = cv2.Canny(resized,0,200)
chars=" A"

def print_pixels(im,chars):
    l=len(chars)
    v=""
    for i in range(im.shape[0]):
        r=""
        for j in range(im.shape[1]):
            c=chars[int(im[i,j]/256*l)]
            r+=c
            r+="  "
        v+=r
        v+="\n"
    return v


v=print_pixels(result,chars)
print(v)

  



