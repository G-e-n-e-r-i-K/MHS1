#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys
import Motor as motors
IR = ev3.Sensor("in1", driver_name = "ht-nxt-ir-seek-v2") 
IR.mode = "DC-ALL"
Compass = ev3.Sensor("in3", driver_name = "ht-nxt-compass")
Compass.mode = "COMPASS"

MA = ev3.LargeMotor("outA")
MB = ev3.LargeMotor("outB")
MC = ev3.LargeMotor("outC")
MD = ev3.LargeMotor("outD")

'''
CODE LOGIC

Theoretically, code turns left/right depending on whether the ball is left/right of the robot using the IR value.
When the ball is in front of the ball, the robot attempts to kick it (when within a certain range)
'''

def cmps_init():
    return(Compass.value())

def get_current_heading(init_value):
    cmps_value = Compass.value()
    curr_heading = cmps_value - init_value
    if curr_heading < 0: curr_heading = 360 + curr_heading
    return(curr_heading)

init_cmps_value = cmps_init()
curr180 = 150

def cmps_correct(curr_heading, trim = 15):
    print("cmps crct now")
    if 90 < curr_heading < curr180:
        print("spinning left")
        motors.spinLeft(0.1)
    elif curr180 < curr_heading < 225:
        print("spinning right")
        motors.spinRight(0.1)
    else: 
        print("in range")
        pass

def cmpscorr():
    curr_heading = get_current_heading(init_cmps_value)

    while 90 < curr_heading < 225:
        curr_heading = get_current_heading(init_cmps_value)
        cmps_correct(curr_heading)


def main():
    IROut = IR.value(0)
    IRVal = IR.value(3)
    if 0 < IROut < 4:
        print('Ball is on the left: 0<IROut<4')
        motors.spinLeft()
    elif 4 < IROut < 6:
        print('Ball is on the in front: 4<IROut<6')
        motors.forward(1000,0.5)                          
        motors.backwards(1000,0.5)                                    
    elif 9 >= IROut > 6:
        print('Ball is on the right: 9>=IROut>6')
        motors.spinRight()
    elif IROut == 0:
        print("no ball seen")
        motors.spinRight(0.5)
        IROut = IR.value(0)
        if IROut != 0: pass
        time.sleep(1)
        motors.spinLeft(0.96)
        IROut = IR.value(0)
        if IROut != 0: pass
        time.sleep(1)
        motors.spinRight(0.5)
        time.sleep(1)

    cmpscorr()

while True:
    main()