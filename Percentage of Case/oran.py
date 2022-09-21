import cv2
import math
import matplotlib.pyplot as plt
import numpy as np

img2 = cv2.imread('nar.jpg') #rotten image
b,g,r = cv2.split(img2)
rows,cols,chs = img2.shape

c3 = np.zeros(shape=(rows,cols))

for i in range(0,rows,1):
    for j in range(0,cols,1):
        blue = img2[i,j,0]
        green = img2[i,j,1]
        red =  img2[i,j,2]
        
        #c3
        c3[i,j] = math.atan(blue/max(red,green))
        
c3=c3*255
        
c1_2 = c3.astype(np.uint8)

kernel = np.ones((5,5), np.uint8)
c1_2 = cv2.dilate(c1_2, kernel, iterations=3)

(thresh, im_bw) = cv2.threshold(c1_2, 130, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

countBlack = 0
countWhite = 0

for i in range(0,rows,1):
    for j in range(0,cols,1):
        if im_bw[i,j] == 0:
            countBlack = countBlack + 1
        else:
            countWhite = countWhite + 1
            

oran = (countBlack/(countBlack + countWhite)) * 100
oran = round(oran)

if oran < 10:
    status = ' Kasa Boş'
elif oran > 10 and oran < 70:
    status = ' Kasa Orta Dolu'
else:
    status = ' Kasa Dolu'
    
    
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img2)

im_bw = cv2.cvtColor(im_bw,cv2.COLOR_BGR2RGB)
plt.subplot(1, 2, 2)
plt.title('(%' + str(oran) + ')' + status)
plt.imshow(im_bw)
plt.show()