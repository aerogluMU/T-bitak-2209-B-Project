#!/usr/bin/env python

import I2C

if __name__ == "__main__":
    i2c= I2C.I2C(addr=(0x70), bus_enable =(0x01