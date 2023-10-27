"""
Created by: Daki A.B
Created on: Oct 2023
This module is a Micro:bit MicroPython program that turns neopixels green if sonar distance >= 10, and red if sonar distance < 10
"""

import neopixel
import machine
from hcsr04 import HCSR04
from microbit import *

# variables
sensor = HCSR04(trigger_pin=1, echo_pin=2)
np = neopixel.NeoPixel(machine.Pin(4), 4)
distance_from_object = sensor.distance_cm()


# on start
display.clear()
display.show(Image.HAPPY)


# if sonar distance is >= 10
while True:
    if button_a.is_pressed():
        if distance_from_object >= 10:
            np[0] = (0, 255, 0)
            np[1] = (0, 255, 0)
            np[2] = (0, 255, 0)
            np[3] = (0, 255, 0)
            print("Distance:", distance_from_object, "cm")
            display.show(Image.HAPPY)
            np[0] = (0, 0, 0)
            np[1] = (0, 0, 0)
            np[2] = (0, 0, 0)
            np[3] = (0, 0, 0)
        else:
            np[0] = (255, 0, 0)
            np[1] = (255, 0, 0)
            np[2] = (255, 0, 0)
            np[3] = (255, 0, 0)
            print("Distance:", distance_from_object, "cm")
            display.show(Image.HAPPY)
            np[0] = (0, 0, 0)
            np[1] = (0, 0, 0)
            np[2] = (0, 0, 0)
            np[3] = (0, 0, 0)
