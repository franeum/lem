#!/usr/bin/env python3

import digitalio
import board
import time 
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.ili9341 as ili9341
import adafruit_rgb_display.st7789 as st7789  # pylint: disable=unused-import
import adafruit_rgb_display.hx8357 as hx8357  # pylint: disable=unused-import
import adafruit_rgb_display.st7735 as st7735  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1351 as ssd1351  # pylint: disable=unused-import
import adafruit_rgb_display.ssd1331 as ssd1331  # pylint: disable=unused-import
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
BAUDRATE = 16000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# pylint: disable=line-too-long
# Create the display:
# disp = st7789.ST7789(spi, rotation=90,                            # 2.0" ST7789
# disp = st7789.ST7789(spi, height=240, y_offset=80, rotation=180,  # 1.3", 1.54" ST7789
# disp = st7789.ST7789(spi, rotation=90, width=135, height=240, x_offset=53, y_offset=40, # 1.14" ST7789
# disp = hx8357.HX8357(spi, rotation=180,                           # 3.5" HX8357
# disp = st7735.ST7735R(spi, rotation=90,                           # 1.8" ST7735R
# disp = st7735.ST7735R(spi, rotation=270, height=128, x_offset=2, y_offset=3,   # 1.44" ST7735R
# disp = st7735.ST7735R(spi, rotation=90, bgr=True,                 # 0.96" MiniTFT ST7735R
# disp = ssd1351.SSD1351(spi, rotation=180,                         # 1.5" SSD1351
# disp = ssd1351.SSD1351(spi, height=96, y_offset=32, rotation=180, # 1.27" SSD1351
# disp = ssd1331.SSD1331(spi, rotation=180,                         # 0.96" SSD1331
#disp = ili9341.ILI9341(
disp = st7735.ST7735R(
    spi,
    rotation=0,  # 2.2", 2.4", 2.8", 3.2" ILI9341
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
)
# pylint: enable=line-too-long

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
print(disp.width)
print(disp.height)

"""
if disp.rotation % 180 == 90:
    height = disp.width  # we swap height/width to rotate it to landscape!
    width = disp.height
else:
    width = disp.width  # we swap height/width to rotate it to landscape!
    height = disp.height
"""
height = disp.height
width = disp.width

print("CONFIGURAZIONE COMPLETATA")


x0 = int(width * 0.25)
y0 = int(height * 0.25)
x1 = int(width * 0.75)
y1 = int(height * 0.75)

#disp.X_START = x0
#disp.Y_START = y0

image = Image.new("RGB", (width,height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a green filled box as the background
#draw.rectangle((0, 0, width, height), outline=0, fill=(255,255,255))
#disp.image(image)


# Load a TTF Font
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", FONTSIZE) 

print("MATERIALI COMPLETATI")

now = time.time()

for _ in range(10):
    # Draw Some Text
    

    draw.rectangle((0,0,width,height), fill=(255,255,255))
    #disp.image(image)
    
    #print("\t\t", time.time() - now)

    text = random.choice(kwlist) #"Hello World!"
    font_width, font_height = font.getsize(text)
    draw.text(
        (width // 2 - font_width // 2, height // 2 - font_height // 2),
        text,
        font=font,
        fill=(0,0,0),
    )

    
    #print("\t\t\t", time.time() - now)

    # Display image.
    disp.image(image)
    #disp.show()
    
    
    #print("After rendering image", time.time() - now)

    newnow = time.time()
    #print(newnow - now)
    now = newnow
    time.sleep(0.1)
