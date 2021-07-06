#!/usr/bin/env python3

import mraa
import time
import busio
import adafruit_ssd1306
import get_nets as net 
from board import SCL3, SDA3
from PIL import Image, ImageDraw, ImageFont

class Push:
    counter = 0
    counter_max = 1000

    def __init__(self, gpio=None, func=-1):
        self.gpio = gpio 
        self.push = mraa.Gpio(gpio)
        self.push.dir(mraa.DIR_IN)
        self.prev = 1
        if func == -1:
            self.a_func = self.subtract
        else:
            self.a_func = self.add

    def read_value(self):
        value = self.push.read()
        if value != self.prev:
            self.prev = value 
            if value == 0:
                Push.counter = self.a_func(Push.counter)
                print(Push.counter)
                return Push.counter

    def add(self, c):
        return min([Push.counter_max, c + 1])

    def subtract(self, c):
        return max([0,c-1])


def write_text(_draw, _disp, _image, _font, w, h, txt):
    _draw.rectangle((0, 0, w, h), outline=0, fill=0)
    _disp.fill(0)
    _disp.show()
    _draw.text((x, top + 12), txt, font=_font, fill=255)
    _disp.image(_image)
    _disp.show()


if __name__ == "__main__":

    PUSH1 = Push(23,-1)
    PUSH2 = Push(24,1)

    # Create the I2C interface.
    i2c = busio.I2C(SCL3, SDA3)
    disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

    # Clear display.
    disp.fill(0)
    disp.show()

    width = disp.width
    height = disp.height
    image = Image.new("1", (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)
    padding = -2
    top = padding
    bottom = height - padding
    # Move left to right keeping track of the current x position for drawing shapes.
    x = 0
    font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf", size=12)

    write_text(draw, disp, image, font, width, height, "Choose wifi SSID")

    list_wifi = net.get_wifi_list()
    Push.counter_max = len(list_wifi) - 1

    time.sleep(2)

    write_text(draw, disp, image, font, width, height, list_wifi[0])

    while True:
        val1 = PUSH1.read_value()
        if val1:
            write_text(draw, disp, image, font, width, height, list_wifi[val1])

        val2 = PUSH2.read_value()
        if val2:
            write_text(draw, disp, image, font, width, height, list_wifi[val2])
