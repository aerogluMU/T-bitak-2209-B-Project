import cv2
import math
import matplotlib.pyplot as plt
import numpy as np

################################
#Color Invarient for Left Image
img = cv2.imread('view0.png') #bitki
#img = cv2.imread('d0.png') #eşyalar
#img = cv2.imread('h0.jpeg') #eşyalar2

b,g,r = cv2.split(img)
rows,cols,chs = img.shape

c1 = np.zeros(shape=(rows,cols))
c2 = np.zeros(shape=(rows,cols))
c3 = np.zeros(shape=(rows,cols))

for i in range(0,rows,1):
    for j in range(0,cols,1):
        blue = img[i,j,0]
        green = img[i,j,1]
        red =  img[i,j,2]
        
        c1[i,j] = math.atan(red/max(green,blue))
        c2[i,j] = math.atan(green/max(red,blue))
        c3[i,j] = math.atan(blue/max(red,green))

c1 = 255 * c1
c1 = c1.astype(np.uint8)
c2 = 255 * c2
c2 = c2.astype(np.uint8)
c3 = 255 * c3
c3 = c3.astype(np.uint8)

imgLeft = c1

################################
#Color Invarient for Right Image
img = cv2.imread('view1.png') #bitki
#img = cv2.imread('d1.png') #eşyalar
#img = cv2.imread('h1.jpeg') #eşyalar2

b,g,r = cv2.split(img)
rows,cols,chs = img.shape

c1 = np.zeros(shape=(rows,cols))
c2 = np.zeros(shape=(rows,cols))
c3 = np.zeros(shape=(rows,cols))

for i in range(0,rows,1):
    for j in range(0,cols,1):
        blue = img[i,j,0]
        green = img[i,j,1]
        red =  img[i,j,2]
        
        c1[i,j] = math.atan(red/max(green,blue))
        c2[i,j] = math.atan(green/max(red,blue))
        c3[i,j] = math.atan(blue/max(red,green))

c1 = 255 * c1
c1 = c1.astype(np.uint8)
c2 = 255 * c2
c2 = c2.astype(np.uint8)
c3 = 255 * c3
c3 = c3.astype(np.uint8)

imgRight = c1

################################
#Depth Map
stereo = cv2.StereoBM_create(numDisparities = 16, blockSize = 15)
disparity = stereo.compute(imgLeft, imgRight)

min = disparity.min()
max = disparity.max()
disparity = np.uint8(255 * (disparity - min) / (max - min))

plt.subplot(2, 2, 1)
plt.title('L_CI')
plt.imshow(imgLeft)

plt.subplot(2, 2, 2)
plt.title('R_CI')
plt.imshow(imgRight)

disparity = cv2.cvtColor(disparity,cv2.COLOR_BGR2RGB)
plt.subplot(2, 2, 3)
plt.title('Depth')
plt.imshow(disparity)

plt.show()

"""
imgLeft = cv2.resize(imgLeft, (600 , 700),interpolation=cv2.INTER_AREA)
imgRight = cv2.resize(imgRight, (600 , 700),interpolation=cv2.INTER_AREA)
disparity = cv2.resize(disparity, (600 , 700),interpolation=cv2.INTER_AREA)
cv2.imshow('L_CI',imgLeft)
cv2.imshow('R_CI',imgRight)
cv2.imshow('Depth',disparity)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""