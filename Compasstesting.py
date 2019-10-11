#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys
import Motor as motors

Compass = ev3.Sensor("in3", driver_name = "ht-nxt-compass")
Compass.mode = "COMPASS"

def cmps_init():
    return(Compass.value())

def get_current_heading(init_value):
    cmps_value = Compass.value()
    curr_heading = cmps_value - init_value
    if curr_heading < 0: curr_heading = 360 + curr_heading
    return(curr_heading)


init_cmps_value = cmps_init()

curr180 = 150

def cmps_correct(trim = 15):
    print("cmps crct now")
    if 90 < curr_heading < curr180:
        print("spinning left----c")
        motors.spinRight()
    elif curr180 < curr_heading < 225:
        print("spinning right---c")
        motors.spinLeft()
    else: 
        print("in range")
        pass

'''
while True:
    # cmps = Compass.value()
    curr_heading = get_current_heading(init_cmps_value)
    print(init_cmps_value , curr_heading , Compass.value())
'''

#225-270, 90-90