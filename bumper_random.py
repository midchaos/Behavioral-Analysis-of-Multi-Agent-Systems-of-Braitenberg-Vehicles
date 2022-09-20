"""TwoWheelRobot_controller controller."""
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

    touchsensor = robot.getTouchSensor('bumper')
    touchsensor.enable(TIMESTEP)
    
    for i in range(len(light_sensors_names)):
        light_sensors.append(robot.getLightSensor(light_sensors_names[i]))
        light_sensors[i].enable(TIMESTEP)
        
    counter = 0
    no_of_collision = 0
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(TIMESTEP) != -1:
        collision = int(touchsensor.getValue())

        left_light_val = light_sensors[0].getValue()/100
        right_light_val = light_sensors[1].getValue()/100
        
        print(left_light_val, right_light_val)
        
        if right_light_val == 0.0 and left_light_val == 0.0:
            left_speed = MAX_SPEED
            right_speed = MAX_SPEED
        else:
            left_speed = right_light_val
            right_speed = left_light_val
        
        if collision == 1:
            counter = 0
            MAX_COUNTER_rand = random.randint(MAX_COUNTER//2, MAX_COUNTER)

            turn = random.choice([-1,1])
            no_of_collision = no_of_collision + 1
            print("bumper_random",no_of_collision)
            
        if counter > MAX_COUNTER_rand//2:
            left_speed = - MAX_SPEED
            right_speed = - MAX_SPEED
            counter = counter - 1
        elif counter <= MAX_COUNTER_rand//2 and counter > 0:
            left_speed = - MAX_SPEED/random.randint(2,4)
            right_speed = turn*MAX_SPEED
            counter = counter - 1
            
        wheels[0].setVelocity(left_speed)
        wheels[1].setVelocity(right_speed)

# Enter here exit cleanup code.
if __name__ == "__main__":
    # create the Robot instance.
    my_robot = Robot()
    run_robot(my_robot)