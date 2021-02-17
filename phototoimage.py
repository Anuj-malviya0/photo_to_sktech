import cv2
import numpy as np


#reading the image 
#load image to same folder firstly 
img='sample.jpg'

imgo = cv2.imread(img)

#sharpneing the image 
sharp = np.array([[-1,-1,-1],
                  [-1,9,-1],
                  [-1,-1,-1]])
new = cv2.filter2D(imgo,-1,sharp)
#converting the image in to gray
gray = cv2.cvtColor(new, cv2.COLOR_BGR2GRAY)
#it's optional we are just checking for any background objects
obj = cv2.cvtColor(new, cv2.COLOR_BGR2HSV)
#creating final image 
inv = 255*gray
gess = cv2.GaussianBlur(inv,ksize=(15,15),sigmaX=0,sigmaY=0)

final = cv2.divide(gray,255*gess,scale=256)
cv2.imshow('image',imgo)
cv2.imshow('sketch',final)
cv2.waitKey(0)
cv2.destroyAllWindows()
