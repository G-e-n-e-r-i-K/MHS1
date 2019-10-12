#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys

Compass = ev3.Sensor("in3", driver_name = "ht-nxt-compass")
Compass.mode = "COMPASS"

MA = ev3.MediumMotor("outA")
MB = ev3.MediumMotor("outB")
MC = ev3.MediumMotor("outC")
MD = ev3.MediumMotor("outD")

CalcPos = [0,0]

def forward(speed = 500,runtime = 1):
    print('Moving forwards for',runtime,'at speed',speed)
    MA.run_timed(time_sp = runtime * 1000, speed_sp=speed) 
    MB.run_timed(time_sp = runtime * 1000, speed_sp=-speed) 
    MC.run_timed(time_sp = runtime * 1000, speed_sp=speed) 
    MD.run_timed(time_sp = runtime * 1000, speed_sp=-speed)     
    time.sleep(runtime) 
    CalcPos[0] += 1

def backwards(speed = 500,runtime = 1):
    print('Moving backwards for',runtime,'at speed',speed)
    MA.run_timed(time_sp = runtime * 1000, speed_sp=-speed) 
    MB.run_timed(time_sp = runtime * 1000, speed_sp=speed) 
    MC.run_timed(time_sp = runtime * 1000, speed_sp=-speed) 
    MD.run_timed(time_sp = runtime * 1000, speed_sp=speed) 
    time.sleep(runtime) 
    CalcPos[0] -= 1

def left(speed = 500,runtime = 1):
    print('Moving left for',runtime,'at speed',speed)
    MA.run_timed(time_sp = runtime * 1000, speed_sp=speed) 
    MB.run_timed(time_sp = runtime * 1000, speed_sp=-speed) 
    MC.run_timed(time_sp = runtime * 1000, speed_sp=-speed) 
    MD.run_timed(time_sp = runtime * 1000, speed_sp=speed) 
    time.sleep(runtime) 
    CalcPos[1] -= 1

def right(speed = 500,runtime = 1):
    print('Moving right for',runtime,'at speed',speed)
    MA.run_timed(time_sp = runtime * 1000, speed_sp=-speed) 
    MB.run_timed(time_sp = runtime * 1000, speed_sp=speed) 
    MC.run_timed(time_sp = runtime * 1000, speed_sp=speed) 
    MD.run_timed(time_sp = runtime * 1000, speed_sp=-speed) 
    time.sleep(runtime) 
    CalcPos[1] += 1

def diag_forward_left(speed = 500,runtime = 1):
    forward(runtime=0.5)
    left(runtime=0.5)

def diag_forward_right(speed = 500,runtime = 1):
    forward(runtime=0.5)
    right(runtime=0.5)

def diag_backward_left(speed = 500,runtime = 1):
    backwards(runtime=0.5)
    left(runtime=0.5)

def diag_backward_right(speed = 500,runtime = 1):
    backwards(runtime=0.5)
    right(runtime=0.5)

def spinRight(runtime = 1):
    print("spinning left")
    MA.run_timed(speed_sp=-500, time_sp = runtime * 1000)
    MB.run_timed(speed_sp=-500, time_sp = runtime * 1000)
    MC.run_timed(speed_sp=-500, time_sp = runtime * 1000)
    MD.run_timed(speed_sp=-500, time_sp = runtime * 1000)

def spinLeft(runtime = 1):
    print("spining right")
    MA.run_timed(speed_sp=500, time_sp = runtime * 1000)
    MB.run_timed(speed_sp=500, time_sp = runtime * 1000)
    MC.run_timed(speed_sp=500, time_sp = runtime * 1000)
    MD.run_timed(speed_sp=500, time_sp = runtime * 1000)

def correction_spin():
    compass = Compass.value(0)
    compass = 0
    if 180 < compass < 360:
        while compass < 350:
            MA.run_timed(speed_sp=300, time_sp=0.1)
            MB.run_timed(speed_sp=300, time_sp=0.1)
            MC.run_timed(speed_sp=300, time_sp=0.1)
            MD.run_timed(speed_sp=300, time_sp=0.1)
            compass = Compass.value(0)
            time.sleep(0.1)
    else:
        while compass > 10:
            MA.run_timed(speed_sp=-300, time_sp=0.1)
            MB.run_timed(speed_sp=-300, time_sp=0.1)
            MC.run_timed(speed_sp=-300, time_sp=0.1)
            MD.run_timed(speed_sp=-300, time_sp=0.1)
            compass = Compass.value(0)
            time.sleep(0.1)
    
#while True:
    #forward(runtime=2)
    #time.sleep(1)
    #diag_forward_left(runtime=2)
    #time.sleep(1)
    #left(runtime=2)
    #time.sleep(1)
    #diag_backward_left(runtime=2)
    #time.sleep(1)
    #backwards(runtime=2)
    #time.sleep(1)
    #diag_backward_right(runtime=2)
    #time.sleep(1)
    #right(runtime=2)
    #time.sleep(1)
    #diag_forward_right(runtime=2)
    #time.sleep(1)
    #MA.run_timed(time_sp = 1000, speed_sp=500)
    #print("a")
    #time.sleep(1)
    #MB.run_timed(time_sp = 1000, speed_sp=500)
    #print("b")
    #time.sleep(1)
    #MC.run_timed(time_sp = 1000, speed_sp=500)
    #print("c")
    #time.sleep(1)
    #MD.run_timed(time_sp = 1000, speed_sp=500)
    #print("d")
    #time.sleep(1) 