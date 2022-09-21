import cv2
import math
import matplotlib.pyplot as plt
import numpy as np

################################
#Color Invarient for Left Image
imgLeft = cv2.imread('view0.png') #bitki
#imgLeft = cv2.imread('d0.png') #eşyalar


################################
#Color Invarient for Right Image
imgRight = cv2.imread('view1.png') #bitki
#imgRight = cv2.imread('d1.png') #eşyalar


# Creating an object of StereoSGBM algorithm

stereo = cv2.StereoSGBM_create(
        minDisparity = 0,
        numDisparities = 64,
        blockSize = 10,
        P1=8*3*8**2,
        P2=32*3*8**2,
        disp12MaxDiff = 32,
        uniquenessRatio = 64,
        speckleWindowSize = 5000,
        speckleRange = 10
    )

# Calculating disparith using the StereoSGBM algorithm

disp = stereo.compute(imgLeft, imgRight).astype(np.float32)
disp = cv2.normalize(disp,0,255,cv2.NORM_MINMAX)

minval = np.min(disp)
maxval = np.max(disp)

rows,cols = disp.shape

for i in range(0,rows,1):
    for j in range(0,cols,1):
        #Resmin i satır j sütunundaki blue, green ve red değerleri
        if disp[i,j]<=((maxval-minval)/2):
            disp[i,j]=0.0
            

# Displaying the disparity map

plt.title('Disparity')
plt.imshow(disp, cmap='hot')
plt.colorbar()

plt.show()