#!/usr/bin/env python3

import mraa 
import time 

class Push:
    def __init__(self, gpio=None):
        self.gpio = gpio 
        self.push = mraa.Gpio(gpio)
        self.push.dir(mraa.DIR_IN)

class Button(Push):
    def __init__(self, gpio=None, sleep=0.1, max_sleep=1, arg=1):
        super().__init__(gpio)
        self.prev = 1
        self._sleep = sleep 
        self._max_sleep = max_sleep 
        self._current_sleep = sleep 
        self._arg = arg

    def get_val(self):
        time.sleep(self._current_sleep)
        self._current_sleep = self._sleep 
        value = self.push.read()

        if value != self.prev:
            self.prev = value 
            if value == 0:
                self._current_sleep = self._max_sleep
                return self.oneshot(self._arg)

    def oneshot(self, arg=1):
        return arg

    @property
    def sleep(self):
        return self._sleep 

    @sleep.setter
    def sleep(self, val):
        self._sleep = val 

    @property
    def max_sleep(self):
        return self._sleep 

    @sleep.setter
    def max_sleep(self, val):
        self._max_sleep = val 

    @property
    def arg(self):
        return self._sleep 

    @arg.setter
    def arg(self, val):
        self._arg = val 




class PushCounter:

    def __init__(self, downer=None, upper=None, current=0):
        self._MIN = 0
        self._MAX = 1000
        self.downer = downer 
        self.upper = upper 
        self.current = current 

    def add(self):
        self.current = min([self._MAX, self.current + 1])
        return self.current

    def subtract(self):
        self.current = max([self._MIN, self.current - 1])
        return self.current 

    def next_value(self):
        if self.downer.get_val():
            return self.subtract() 
        if self.upper.get_val():
            return self.add() 

    @property
    def min(self):
        return self._MIN 

    @property
    def max(self):
        return self._MAX 

    @min.setter
    def min(self, val):
        self._MIN = val 

    @max.setter
    def min(self, val):
        self._MAX = val 


class ButtonTimer(Push):
    def __init__(self, gpio=None, sleep=0.1, max_sleep=1, arg=1):
        super().__init__(gpio)
        self.prev = 1
        self._sleep = sleep 
        self._max_sleep = max_sleep 
        self._current_sleep = sleep 
        self._arg = arg