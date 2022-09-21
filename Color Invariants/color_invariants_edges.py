import cv2
import math
import matplotlib.pyplot as plt
import numpy as np

#img = cv2.imread('yellow.png') #sarı cisim
img = cv2.imread('green.jpeg') #yeşil cisim
#img = cv2.imread('blue.jpeg') #mavi cisim

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
        blue = img[i,j,0]
        green = img[i,j,1]
        red =  img[i,j,2]
        
        #c1
        c1[i,j] = math.atan(red/max(green,blue))
        
        #c2
        c2[i,j] = math.atan(green/max(red,blue))
        
        #c3
        c3[i,j] = math.atan(blue/max(red,green))

#float olan c1,c2,c3 değerlerini uint8 haline çevirdim
c1 = 255 * c1
c1 = c1.astype(np.uint8)

c2 = 255 * c2
c2 = c2.astype(np.uint8)

c3 = 255 * c3
c3 = c3.astype(np.uint8)

#c1,c2,c3'ü birleştirdim
new_img = cv2.merge((c1,c2,c3))

#new_img Canny Edge
edges_merge = cv2.Canny(new_img,150,200)
#Orjinal Image Canny Edge
img2 = cv2.cvtColor(img2,cv2.COLOR_RGB2BGR)
edges = cv2.Canny(img2,150,200)

plt.subplot(2,2,1),plt.imshow(img2,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Original Image'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3),plt.imshow(new_img,cmap = 'gray')
plt.title('Merge Image'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4),plt.imshow(edges_merge,cmap = 'gray')
plt.title('Edge Merge Image'), plt.xticks([]), plt.yticks([])

plt.show()

"""
#c1 Canny Edge
edges1 = cv2.Canny(c1,150,200)
#c2 Canny Edge
edges2 = cv2.Canny(c2,100,200)
#c3 Canny Edge
edges3 = cv2.Canny(c3,150,200)

plt.subplot(3,2,1),plt.imshow(c1,cmap = 'gray')
plt.title('c1'), plt.xticks([]), plt.yticks([])

plt.subplot(3,2,2),plt.imshow(edges1,cmap = 'gray')
plt.title('c1 Edge'), plt.xticks([]), plt.yticks([])

plt.subplot(3,2,3),plt.imshow(c2,cmap = 'gray')
plt.title('c2'), plt.xticks([]), plt.yticks([])

plt.subplot(3,2,4),plt.imshow(edges2,cmap = 'gray')
plt.title('c2 Edge'), plt.xticks([]), plt.yticks([])

plt.subplot(3,2,5),plt.imshow(c3,cmap = 'gray')
plt.title('c3'), plt.xticks([]), plt.yticks([])

plt.subplot(3,2,6),plt.imshow(edges3,cmap = 'gray')
plt.title('c3 Edge'), plt.xticks([]), plt.yticks([])

plt.show()
"""