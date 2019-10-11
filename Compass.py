#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys
import Motor.py as motors

Compass = ev3.Sensor("in4", driver_name = "ht-nxt-compass")
Compass.mode = "COMPASS"

def compass_correct():
    CVal = Compass.value(0)
    if 180 < CVal < 360: 
        motors.MA.run_timed(speed_sp=100, time_sp=1)
        motors.MB.run_timed
    else:


while True:
    CVal = Compass.value(0)
    print(CVal)