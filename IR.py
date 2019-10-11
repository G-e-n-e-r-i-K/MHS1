#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys

IR = ev3.Sensor("in2", driver_name = "ht-nxt-ir-seek-v2") 
IR.mode = "AC-ALL"
IROut = IR.value(0)
IRVal = IR.value(3)

i = 0





#if 1 <= IROut <= 4:

while True:
    IROut = IR.value(0)
    IRVal = IR.value(3)
    if IRVal > 60:
        i += 1
        print("IR!!!")
    else:
        print("no :(")
    