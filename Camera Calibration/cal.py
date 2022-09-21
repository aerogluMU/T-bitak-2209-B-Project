import io
import time
import picamera
import cv2
import numpy as np
import mux


changer = mux.MUX()


for ii in range(13):
    
    print("(%d) Numaralı Fotoğraflar için hazırlan..."%(ii+1))
    
    for jj in range(3):
        print("%d"%(3-jj))
        time.sleep(1)
        
    stream1=io.BytesIO()
    changer.camera_change(1)

    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(0.01)
        camera.capture('left-%d.jpg'%(ii+1))
        camera.stop_preview()


    stream2=io.BytesIO()
    changer.camera_change(2)

    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(0.01)        
        camera.capture('right-%d.jpg'%(ii+1))
        camera.stop_preview()
    
    print("(%d) Numaralı Fotoğraflar Çekildi..."%(ii+1))
    print("************************************")
    time.sleep(2)

print("Fotoğrafların Çekimi Tamamlandı...")
