#!/usr/bin/env python3

import time
import random
import subprocess
import busio
import adafruit_ssd1306
from keyword import kwlist
from board import SCL3, SDA3
from PIL import Image, ImageDraw, ImageFont


"""
table of conversion point -> pixel
point   C               space           2               n.of chars
5       (3, 6)          (3, 5)          (3, 5)          42
6       (4, 6)          (4, 5)          (4, 5)          32
7       (4, 7)          (4, 6)          (4, 6)          32
8       (5, 8)          (5, 7)          (5, 7)          25
9       (6, 8)          (5, 8)          (5, 8)          21
10      (6, 9)          (6, 9)          (6, 9)          21
11      (7, 10)         (7, 10)         (7, 10)         18
12      (7, 10)         (7, 10)         (7, 10)         18
13      (8, 11)         (8, 11)         (8, 11)         16
14      (8, 12)         (8, 12)         (8, 12)         16
15      (9, 13)         (9, 13)         (9, 13)         14
16      (10, 14)        (10, 14)        (10, 14)        12
17      (10, 15)        (10, 15)        (10, 15)        12
18      (11, 15)        (11, 15)        (11, 15)        11
19      (11, 16)        (11, 16)        (11, 16)        11
20      (12, 17)        (12, 17)        (12, 17)        10
"""

FONTSIZE = 12
TOP = -2
X = 0

class OledDisplay:
    def __init__(self, scl=SCL3, sda=SDA3, pixelX=128, pixelY=32):
        self.i2c = busio.I2C(scl, sda) 
        self.disp = adafruit_ssd1306.SSD1306_I2C(pixelX, pixelY, self.i2c)
        self.width = self.disp.width
        self.height = self.disp.height
        #self._font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf", size=12) 
        self._font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", size=FONTSIZE)
        self.__image()
        self.__draw()
        self.clear()
    
    def __image(self):
        self.image = Image.new("1", (self.width, self.height))

    def __draw(self):
        # Get drawing object to draw on image.
        self.draw = ImageDraw.Draw(self.image)
        # Draw a black filled box to clear the image.
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)

    def clear(self):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.disp.fill(0)
        self.disp.show()

    def write_text(self, txt):
        self.draw.text((X, TOP + 8), txt, font=self._font, fill=255)
        self.disp.image(self.image)
        self.disp.show()

    def create_scrolling_text(self, string, a_time=0.1):
        # 15
        for i,ch in enumerate(string):
            c = i + 1
            self.write_text(string[:c])
            time.sleep(a_time)

    @property
    def font(self):
        return self._font 
    
    @font.setter
    def font(self, fontpath, size):
        self._font = ImageFont.truetype(fontpath, size=size)


if __name__ == "__main__":
    o = OledDisplay()
    o.write_text("TEST")
    time.sleep(2)
    o.clear()
    print("cleared")
    o.create_scrolling_text("Scrolling........")
    time.sleep(2)
    o.clear()
    now = time.time()
    for _ in range(20):
        txt = random.choice(kwlist)
        o.write_text(txt)
        time.sleep(0.01)
        o.clear()
        yetnow = time.time()
        print(yetnow - now)
        now = yetnow

    o.clear()
