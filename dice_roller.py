from machine import Pin
import tm1637
from random import randint
from utime import sleep
import _thread
from neopixel import Neopixel

mydisplay = tm1637.TM1637(clk=Pin(26), dio=Pin(27))
button = Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
pixels = Neopixel(8, 0, 15, "GRB")

def core0_thread():
    while True:
        if not button.value():
            mydisplay.show("    ")
            print("Rolling")
            for i in range(10):
                mydisplay.number(randint(1,20))
                sleep(0.1)
            sleep(5)
        else:
            mydisplay.scroll("Press to roll", delay=200)
def core1_thread():
    while True:
        for i in range(8):
            pixels.set_pixel(i,(((randint(1,254), randint(1,254), randint(1,254)))))
            pixels.show()
            sleep(0.1)

second_thread = _thread.start_new_thread(core1_thread, ())
core0_thread()