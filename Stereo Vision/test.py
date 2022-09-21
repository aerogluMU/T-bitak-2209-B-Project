import io
import time
import picamera
import cv2
import numpy as np
import mux


changer = mux.MUX()


while True:
    stream1=io.BytesIO()
    changer.camera_change(1)

    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(0.01)
        camera.capture(stream1,format='jpeg')
    
    data1=np.frombuffer(stream1.getvalue(),dtype=np.uint8)
    image1=cv2.imdecode(data1,1)


    stream2=io.BytesIO()
    changer.camera_change(2)

    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(0.01)        
        camera.capture(stream2,format='jpeg')
        
    
    data2=np.frombuffer(stream2.getvalue(),dtype=np.uint8)
    image2=cv2.imdecode(data2,1)

    cv2.imshow('Image1',image1)
    cv2.imshow('Image2',image2)
    
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break


    
   

    
    
    
    