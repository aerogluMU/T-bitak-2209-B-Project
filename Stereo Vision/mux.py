import sys
import I2C
import picamera
import RPi.GPIO as GPIO
from functools import reduce

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


class MUX():
    
    pin_Dict = {'A': (11, 12), 'C': (21, 22), 'B': (15, 16), 'D': (23, 24)}
    pins = list(reduce(lambda x,y: x+y, pin_Dict.values()))
    pins.sort()
    enum_Pins = {i+1 : x for i,x in enumerate(pins)}
    del(pins)

    def __init__(self, jumper=1):
        
        self.jumper = jumper
        self.fPin = 0
        self.camera = 1
        self.is_opened = False
        self.link_gpio()
        self.i2c = I2C.I2C(addr=(0x70), bus_enable =(0x01)) # Creates i2c object
    
    def link_gpio(self):
        
        self.fPin = self.enum_Pins[self.jumper]
        GPIO.setup(self.fPin, GPIO.OUT)
        
    def camera_change(self, camera=1):
        
        if camera == 1:
            
            self.i2c.write_control_register((0x01))
            GPIO.output(self.fPin, False)
            
        elif camera == 2:
            self.i2c.write_control_register((0x02))
            GPIO.output(self.fPin, True)
        else:
            self.close()
            sys.exit(0)
            
        self.camera = camera
