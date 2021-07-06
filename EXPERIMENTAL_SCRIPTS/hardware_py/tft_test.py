#!/usr/bin/env python3

import digitalio
import board
import time 
import displayio
import adafruit_ili9341
from keyword import kwlist
import random 

# First define some constants to allow easy resizing of shapes.
BORDER = 20
FONTSIZE = 24

# Configuration for CS and DC pins (these are PiTFT defaults):
cs_pin = digitalio.DigitalInOut(board.pin.SPI2_CS)  
dc_pin = digitalio.DigitalInOut(board.pin.GPIO2_A1)  
reset_pin = digitalio.DigitalInOut(board.pin.GPIO0_B3)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

displayio.release_displays()
display_bus = displayio.FourWire(spi, command=dc_pin, chip_select=cs_pin)

display = adafruit_ili9341.ILI9341(display_bus, width=320, height=240)

# Make the display context
splash = displayio.Group(max_size=10)
display.show(splash)

color_bitmap = displayio.Bitmap(320, 240, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF0000

bg_sprite = displayio.TileGrid(color_bitmap,
                               pixel_shader=color_palette,
                               x=0, y=0)
splash.append(bg_sprite)

while True:
    # Fill the screen red, green, blue, then black:
    for color in ((255, 0, 0), (0, 255, 0), (0, 0, 255)):
        display.fill(color565(color))
    # Clear the display
    display.fill(0)
    # Draw a red pixel in the center.
    display.pixel(display.width // 2, display.height // 2, color565(255, 0, 0))
    # Pause 2 seconds.
    time.sleep(2)
    # Clear the screen a random color
    display.fill(
        color565(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    )
    # Pause 2 seconds.
    time.sleep(2)