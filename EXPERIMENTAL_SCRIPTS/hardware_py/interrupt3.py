#!/usr/bin/env python3

import mraa
import time
import sys
import os 
import threading 
import curses
import oled 


# constants
MAX_TIME    = 3
DEBUG       = 0
D_OLED      = oled.OledDisplay() 

class Counter:
    def __init__(self):
        self.c  = 0
        self._start = 0
        self.elapsed = 0
        self.flag = False   
        self._pin = 24
        self.x = mraa.Gpio(24)
        self.x.dir(mraa.DIR_IN)
        self.x.edge(mraa.EDGE_BOTH)

    def on_press(self, func):
        self.x.isr(mraa.EDGE_BOTH, func, self)

    def perform_exit(self):
        self.x.isrExit()

    @property
    def start(self):
        return self._start 

    @start.setter
    def start(self, value):
        self._start = value 


def callback(cls):
    gpio = cls.x
    if gpio.read() == 0:
        if DEBUG: print("pressed")
        cls.start = time.time()
        cls.flag = True

    elif gpio.read() == 1:
        if DEBUG: print("released")
        cls.flag = False 


def timing(cls):
    while True:
        if cls.flag:
            now = time.time()
            cls.elapsed = now - cls.start 
            if check_elapsed(cls.elapsed):
                print("OK, ESEGUO ALTRO PROGRAMMA")
                D_OLED.create_scrolling_text("Create ACP......", a_time=0.1)
                cls.start = time.time() 
        else:
            if DEBUG: print("non premuto")
        time.sleep(0.25)


def check_elapsed(e_time):
    if e_time >= MAX_TIME:
        return True 
    else:
        return False 




def main():
    try:
        c = Counter()

        t1 = threading.Thread(target=c.on_press, args=(callback,))
        t1.start()
        t1.join() 
        
        t2 = threading.Thread(target=timing, args=(c,))
        t2.start() 
        t2.join()

        var = input("Press ENTER to stop")
        c.perform_exit()

    except ValueError as e:
        print(e)

    
if __name__ == "__main__":
    main()
