import cv2
import math
import matplotlib.pyplot as plt
import numpy as np

def my_atan(x):
    return x - (x*x*x)/3 + (x*x*x*x*x)/5 - (x*x*x*x*x*x*x)/7

img = cv2.imread('ayva.jpg') #ayva
#img = cv2.imread('domates.jpg') #domates
#img = cv2.imread('nar.jpg') #nar
#img = cv2.imread('lahana.jpg') #lahana

#img = cv2.imread('yellow.png') #sarı cisim
#img = cv2.imread('green.jpeg') #yeşil cisim
#img = cv2.imread('blue.jpeg') #mavi cisim
#img = cv2.imread('Comb.jpeg') #comb

img2 = img.copy()

#Resmi b=blue,g=green,r=red kanallarına ayırdım
b,g,r = cv2.split(img)

#Resmin satır,sütun ve kanallarını ilgili değerlere atadım
rows,cols,chs = img.shape

#c1,c2,c3 için resim boyutunda(rowxcol) array oluşturup her bir değere sıfır atadım
c1 = np.zeros(shape=(rows,cols))
c2 = np.zeros(shape=(rows,cols))
c3 = np.zeros(shape=(rows,cols))

#Resmin her bir pixeline ulaşmak için satır ve sütunlar için iç içe 2 for açtım
for i in range(0,rows,1):
    for j in range(0,cols,1):
        #Resmin i satır j sütunundaki blue, green ve red değerleri
        blue = img[i,j,0] / 255
        green = img[i,j,1] / 255
        red =  img[i,j,2] / 255
        
        #c1
        
        c1[i,j] = my_atan(red/max(green,blue))
        
        #c2
        c2[i,j] = my_atan(green/max(red,blue))
        
        #c3
        c3[i,j] = my_atan(blue/max(red,green))

#float olan c1,c2,c3 değerlerini uint8 haline çevirdim
c1 = 255 * c1
c1 = c1.astype(np.uint8)

c2 = 255 * c2
c2 = c2.astype(np.uint8)

c3 = 255 * c3
c3 = c3.astype(np.uint8)

#c1,c2,c3'ü birleştirdim
new_img = cv2.merge((c1,c2,c3))


#matplotlib ile fotoğrafları 3x2lik grafiğe yerleştiriyorum
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
plt.subplot(3, 2, 1)
plt.title('Original Image')
plt.imshow(img2)

c1 = cv2.cvtColor(c1,cv2.COLOR_BGR2RGB)
plt.subplot(3, 2, 2)
plt.title('c1')
plt.imshow(c1)

c2 = cv2.cvtColor(c2,cv2.COLOR_BGR2RGB)
plt.subplot(3, 2, 3)
plt.title('c2')
plt.imshow(c2)

c3 = cv2.cvtColor(c3,cv2.COLOR_BGR2RGB)
plt.subplot(3, 2, 4)
plt.title('c3')
plt.imshow(c3)

plt.subplot(3, 2, 5)
plt.title('Merge')
plt.imshow(new_img)
plt.show()

"""
cv2.imshow('Original Image',img2)
cv2.imshow('c1',c1)
cv2.imshow('c2',c2)
cv2.imshow('c3',c3)
cv2.imshow('Merge',new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""