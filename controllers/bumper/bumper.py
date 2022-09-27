"""TwoWheelRobot_controller controller."""
from tkinter.tix import MAX
from controller import Robot
from controller import TouchSensor
import random

TIMESTEP = 64
MAX_SPEED = 10
NORMAL_SPEED = 1

MAX_COUNTER = 30

def run_robot(robot):     
    #Enable motors
    wheels =[]
    wheelsName = ['wheel1', 'wheel2']
    
    for i in range(len(wheelsName)):
        wheels.append(robot.getMotor(wheelsName[i]))
        wheels[i].setPosition(float('inf'))
        wheels[i].setVelocity(0.0)
        
    light_sensors = []
    light_sensors_names = ['is_left', 'is_right']

    touchsensor = robot.getTouchSensor('bumper')
    touchsensor.enable(TIMESTEP)
    
    for i in range(len(light_sensors_names)):
        light_sensors.append(robot.getLightSensor(light_sensors_names[i]))
        light_sensors[i].enable(TIMESTEP)


    counter = 0
    no_of_collision = 0
    while robot.step(TIMESTEP) != -1:

        collision = int(touchsensor.getValue())

        left_light_val = light_sensors[0].getValue()/100
        right_light_val = light_sensors[1].getValue()/100
        
        # AGGRESSION
        left_speed = max(right_light_val,NORMAL_SPEED)
        right_speed = max(left_light_val,NORMAL_SPEED)
        
        if collision == 1:
            counter = MAX_COUNTER
            no_of_collision = no_of_collision + 1
            print("bumper",no_of_collision)
            
        if counter > MAX_COUNTER//2:
            left_speed = - MAX_SPEED
            right_speed = - MAX_SPEED
            counter = counter - 1
        elif counter <= MAX_COUNTER//2 and counter > 0:
            left_speed = -MAX_SPEED/2
            right_speed = -MAX_SPEED
            counter = counter - 1
        
        wheels[0].setVelocity(left_speed)
        wheels[1].setVelocity(right_speed)

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)