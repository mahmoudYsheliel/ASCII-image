import numpy as np
import cv2
import imutils
from  scipy import signal
import time
import os
 
# Clearing the Screen


def show_im(name,im):
    cv2.imshow(name,im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def print_pixels(im,chars):
    l=len(chars)
    v=""
    for i in range(im.shape[0]):
        r=""
        for j in range(im.shape[1]):
            c=chars[int(im[i,j]/256*l)]
            r+=c
            r+=" "
        v+=r
        v+="\n"
    return v

wan=cv2.imread("wan.png")
wan=cv2.cvtColor(wan,cv2.COLOR_RGB2GRAY)

resized = imutils.resize(wan, width=200)
chars=" .:-=+*#%@"
#chars="$@B8&M#oahkbdqwmZO0QLCJUYXzcvunxrjft\|)1}]?_+>!lI;:,'. "[::-1]
#chars=" .-+#@"



v=print_pixels(resized,chars)
print(v)

#cap = cv2.VideoCapture('video.mp4')  
#while(cap.isOpened()):
      
#   ret, frame = cap.read()
#   frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
#   frame = imutils.resize(frame, width=200)
#   os.system('cls')
#   v=print_pixels(frame,chars)
#   print(v)
#   time.sleep(0.05) 
#cap.release()
  



