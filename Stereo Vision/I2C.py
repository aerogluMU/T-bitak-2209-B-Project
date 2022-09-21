from datetime import datetime

import smbus

i2c_address = (0x70)
i2c_register = (0x00)

i2c_bus0 = (0x01)
i2c_bus1 = (0x02)

class I2C():
    def __init__(self, bus_pin=1, addr=i2c_address, bus_enable=i2c_bus0):
        self.i2c = smbus.SMBus(bus_pin)
        self.addr = addr
        config = bus_enable
        self.write(i2c_register, config)

    def write(self, register, data):
        self.i2c.write_byte_data(self.addr, register, data)

    def read(self):
        return self.i2c.read_byte(self.addr)

    def read_control_register(self):
        value = self.read()
        return value

    def write_control_register(self, config):
        self.write(i2c_register, config)
