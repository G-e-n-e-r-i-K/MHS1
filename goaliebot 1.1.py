#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time
import sys
import Motor as motors
import CS as colour
import US as US
from threading import Thread
button = ev3.Button()
IR = ev3.Sensor("in1", driver_name = "ht-nxt-ir-seek-v2") 
#print(dir(IR))
IR.mode = "DC-ALL"
#IRVal = IR.value(6)
button = ev3.Button()
Paused = False
CS = ev3.ColorSensor("in2")
CS.mode = "COL-COLOR"

Compass = ev3.Sensor("in3", driver_name = "ht-nxt-compass")
Compass.mode = "COMPASS"

MA = ev3.LargeMotor("outA")
MB = ev3.LargeMotor("outB")
MC = ev3.LargeMotor("outC")
MD = ev3.LargeMotor("outD")

USR = ev3.UltrasonicSensor("in4")
USR.mode = "US-DIST-CM"

'''
CURRENT PROGRAM MADE FOR CONFIG: 
Compass 
IR
Colour
US
'''

def refresh():
    IROut = IR.value(0)
    IRVal = IR.value(3)
    CSOut = CS.value(0)

def TrackBall():

    # Ball is left
    IROut = IR.value(0)
    IRVal = IR.value(3)
    if 0 < IROut < 4:
        print('Ball is on the left: 0<IROut<4')
        motors.left(1000,0.125)                             #move left 1cm
        if colour.CheckColourNew() == 1:          #check colour
            motors.right(1000,0.5)
        elif colour.CheckColourNew() == 3:
            pass    
    elif 4 < IROut < 6:
        print('Ball is on the in front: 4<IROut<6')
        motors.forward(1000,0.5)                          #move forward 1cm
        motors.backwards(1000,0.5)                        #move backwards 1cm
        if colour.CheckColourNew() == 1:          #check colour
            motors.backwards(1000,0.5)
        elif colour.CheckColourNew() == 3:
            pass    
    elif 9 >= IROut > 6:
        print('Ball is on the right: 9>=IROut>6')
        motors.right(1000,0.125)                            #move right 1cm
        if colour.CheckColourNew() == 1:          #check colour
            motors.left(1000,0.5)
        elif colour.CheckColourNew() == 3:
            pass       
    elif IROut == 0:
        print('Ball not visible: IROut=0')
        #if US.USFCheck == 3:
        motors.left(1000,0.25)
        motors.right(1000,0.5)
        motors.left(1000,0.25)
        #elif US.USFCheck == 1:
        #motors.left()
        #elif US.USFCheck == 2:
        #motors.right()
    else:
        print("IR Error")

def refreshCompassButton(state):
    print("refreshing")
    cmps = Compass.value(0)
    if button.enter:
        cmps = 0
        while button.enter:
            pass
'''
while not button.backspace():
    refresh()
    TrackBall()
'''

#def main()
 #   irThread = Thread(target=refresh, args=(,))
  #  colThread = Thread(target=cs.CheckColourNew, args=(,))
   # while True:
    #    trackball()

#if __name__ == "__main__":
 #   main()

while True:
    refresh()
    TrackBall()