#!/usr/bin/env python3

import serial
import time
import liblo 
from rock_potentiometer import Pot

def decode_bytes(packed): 
    label = (packed >> 16) & 255
    value = packed & 511
    return label, value 

def main():
    size = 3
    arduino = serial.Serial('/dev/ttyUSB0', 115200, timeout=None)
    pot = [Pot(label=x) for x in range(size)]

    while True:
        try:
            datum = int.from_bytes(arduino.read(3), byteorder='big')
            label, value = decode_bytes(datum)
            pot[label].check_value(value) 
            time.sleep(0.005)
        except KeyboardInterrupt:
            print("\n=== Interrupt from Keyboard ===")
            exit()

if __name__ == "__main__":
    main()
