import cv2
import math
import matplotlib.pyplot as plt
import numpy as np

img2 = cv2.imread('ayva2.jpg') #rotten image
img = img2.copy()
img2 = cv2.GaussianBlur(img2,(5,5),0)
b,g,r = cv2.split(img2)
rows,cols,chs = img2.shape

c2 = np.zeros(shape=(rows,cols))

for i in range(0,rows,1):
    for j in range(0,cols,1):
        blue = img2[i,j,0]
        green = img2[i,j,1]
        red =  img2[i,j,2]
        
        c2[i,j] = math.atan(green/max(red,blue))
        c2[i,j] = c2[i,j] * 255
        
        if c2[i,j] < 120:
            c2[i,j] = 120;
        elif c2[i,j] > 200:
            c2[i,j] = 200;

        
c1_2 = c2.astype(np.uint8)

(thresh, im_bw) = cv2.threshold(c1_2, 130, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

kernel = np.ones((5,5), np.uint8)
im_bw = cv2.erode(im_bw, kernel, iterations=1)

countors, _ = cv2.findContours(im_bw,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

count = 0

for cnt in countors:
    (x,y,w,h)=cv2.boundingRect(cnt)
    area = cv2.contourArea(cnt)
    if area > 1000 and area < 20000:
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(img,"Rotten Area",(x,y),1,1,(0,255,0))
        count = count + 1

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.subplot(1, 3, 1)
plt.title(str(count) + ' Rotten Area')
plt.imshow(img)

c1_2 = cv2.cvtColor(c1_2,cv2.COLOR_BGR2RGB)
plt.subplot(1, 3, 2)
plt.title('CI')
plt.imshow(c1_2)

im_bw = cv2.cvtColor(im_bw,cv2.COLOR_BGR2RGB)
plt.subplot(1, 3, 3)
plt.title('binary')
plt.imshow(im_bw)

plt.show()