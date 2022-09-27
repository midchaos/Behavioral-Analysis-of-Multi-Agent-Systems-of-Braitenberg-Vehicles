"""OneWheelRobot_controller controller."""

from controller import Robot

TIMESTEP = 64
MAX_SPEED = 10

def run_robot(robot):       
    #Enable motors
    wheels =[]
    wheelsName = ['wheel1']
    
    for i in range(len(wheelsName)):
        wheels.append(robot.getMotor(wheelsName[i]))
        wheels[i].setPosition(float('inf'))
        wheels[i].setVelocity(0.0)
        
    light_sensors = []
    light_sensors_names = ['light']
    
    for i in range(len(light_sensors_names)):
        light_sensors.append(robot.getLightSensor(light_sensors_names[i]))
        light_sensors[i].enable(TIMESTEP)

    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(TIMESTEP) != -1:
        light_val = light_sensors[0].getValue()/100 
        bot_speed = MAX_SPEED - light_val
        wheels[0].setVelocity(bot_speed)

if __name__ == "__main__":
    # create the Robot instance.
    my_robot = Robot()
    run_robot(my_robot)