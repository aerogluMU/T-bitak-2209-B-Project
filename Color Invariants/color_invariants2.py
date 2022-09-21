import cv2
import math
import matplotlib.pyplot as plt
import numpy as np
np.seterr(over='ignore')

img = cv2.imread('yellow.png')
#img = cv2.imread('green.jpeg')
#img = cv2.imread('blue.jpeg')

img2 = img.copy()
#Resmi b=blue,g=green,r=red kanallarına ayırdım
b,g,r = cv2.split(img)

#Resmin satır,sütun ve kanallarını ilgili değerlere atadım
row,col,ch = img.shape

#c1,c2,c3 için resim boyutunda(rowxcol) array oluşturup her bir değere sıfır atadım
i1 = np.zeros(shape=(row,col))
i2 = np.zeros(shape=(row,col))
i3 = np.zeros(shape=(row,col))

#Resmin her bir pixeline ulaşmak için satır ve sütunlar için iç içe 2 for açtım
for i in range(0,row,1):
    for j in range(0,col,1):
        #Resmin i satır j sütunundaki blue, green ve red değerleri
        blue = img[i,j,0]
        green = img[i,j,1]
        red =  img[i,j,2]
        
        #i1
        i1[i,j] = ((red - green)**2) / (((red - green)**2) + ((red - blue)**2) + ((green - blue)**2))
        
        #i2
        i2[i,j] = ((red - blue)**2) / (((red - green)**2) + ((red - blue)**2) + ((green - blue)**2))
        
        #i3
        i3[i,j] = ((green - blue)**2) / (((red - green)**2) + ((red - blue)**2) + ((green - blue)**2))

#float olan c1,c2,c3 değerlerini uint8 haline çevirdim
i1 = 255 * i1
i1 = i1.astype(np.uint8)

i2 = 255 * i2
i2 = i2.astype(np.uint8)

i3 = 255 * i3
i3 = i3.astype(np.uint8)

#c1,c2,c3'ü birleştirdim
new_img = cv2.merge((i1,i2,i3))


#matplotlib ile fotoğrafları 3x2lik grafiğe yerleştiriyorum
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
plt.subplot(3, 2, 1)
plt.title('Original Image')
plt.imshow(img2)

c1 = cv2.cvtColor(i1,cv2.COLOR_BGR2RGB)
plt.subplot(3, 2, 2)
plt.title('i1')
plt.imshow(i1)

c2 = cv2.cvtColor(i2,cv2.COLOR_BGR2RGB)
plt.subplot(3, 2, 3)
plt.title('i2')
plt.imshow(i2)

c3 = cv2.cvtColor(i3,cv2.COLOR_BGR2RGB)
plt.subplot(3, 2, 4)
plt.title('i3')
plt.imshow(i3)

plt.subplot(3, 2, 5)
plt.title('Merge')
plt.imshow(new_img)

plt.show()

"""
cv2.imshow('Original Image',img2)
cv2.imshow('i1',i1)
cv2.imshow('i2',i2)
cv2.imshow('i3',i3)
cv2.imshow('Merge',new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""