""""""
from tkinter.tix import MAX
from controller import Robot
from controller import TouchSensor
import random

TIMESTEP = 64
MAX_SPEED = 10
NORMAL_SPEED = 1

MAX_COUNTER = 20

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

    distance_sensor = robot.getDistanceSensor('ds1')
    distance_sensor.enable(TIMESTEP)
    
    for i in range(len(light_sensors_names)):
        light_sensors.append(robot.getLightSensor(light_sensors_names[i]))
        light_sensors[i].enable(TIMESTEP)

    counter = 0
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(TIMESTEP) != -1:

        obstacle_distance = int(distance_sensor.getValue())
        print(obstacle_distance)
        
        left_light_val = light_sensors[0].getValue()/100
        right_light_val = light_sensors[1].getValue()/100
        
        # print(left_light_val, right_light_val)
        
        if right_light_val == 0.0 and left_light_val == 0.0:
            left_speed = MAX_SPEED
            right_speed = MAX_SPEED
        else:
            left_speed = right_light_val
            right_speed = left_light_val
              
        if obstacle_distance//10 > 100 :
            left_speed = - MAX_SPEED/random.randint(2,4)
            right_speed = MAX_SPEED
        
        # print("Distance",left_speed, right_speed) 
        wheels[0].setVelocity(left_speed)
        wheels[1].setVelocity(right_speed)

# Enter here exit cleanup code.
if __name__ == "__main__":
    # create the Robot instance.
    my_robot = Robot()
    run_robot(my_robot)