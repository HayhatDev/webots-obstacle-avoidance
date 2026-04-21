from controller import Robot

robot = Robot()
time_step = 64

left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")
left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

ps0 = robot.getDevice("ps0")
ps1 = robot.getDevice("ps1")
ps2 = robot.getDevice("ps2")
ps3 = robot.getDevice("ps3")
ps4 = robot.getDevice("ps4")
ps5 = robot.getDevice("ps5")
ps6 = robot.getDevice("ps6")
ps7 = robot.getDevice("ps7")

ps0.enable(time_step)
ps1.enable(time_step)
ps2.enable(time_step)
ps3.enable(time_step)
ps4.enable(time_step)
ps5.enable(time_step)
ps6.enable(time_step)
ps7.enable(time_step)

speed = 2.0
danger = 100.0

stuck_counter = 0

while robot.step(time_step) != -1:
    v0 = ps0.getValue()
    v1 = ps1.getValue()
    v2 = ps2.getValue()
    v3 = ps3.getValue()
    v4 = ps4.getValue()
    v5 = ps5.getValue()
    v6 = ps6.getValue()
    v7 = ps7.getValue()
    
    fl = v0
    fr = v7
    sl = v1
    sr = v6
    rl = v3
    rr = v4
    
    if fl > danger and fr > danger and sl > danger and sr > danger:
        stuck_counter += 1
    else:
        stuck_counter = 0
    
    if stuck_counter > 30:
        left_motor.setVelocity(-speed)
        right_motor.setVelocity(-speed)
        for _ in range(20):
            robot.step(time_step)
        left_motor.setVelocity(-speed)
        right_motor.setVelocity(speed)
        for _ in range(30):
            robot.step(time_step)
        stuck_counter = 0
        continue
    
    if fl > danger or fr > danger:
        left_motor.setVelocity(speed)
        right_motor.setVelocity(-speed)
        robot.step(time_step * 10)
    elif sl > danger:
        left_motor.setVelocity(-speed)
        right_motor.setVelocity(speed)
    elif sr > danger:
        left_motor.setVelocity(speed)
        right_motor.setVelocity(-speed)
    elif rl > danger or rr > danger:
        left_motor.setVelocity(speed)
        right_motor.setVelocity(speed)
    else:
        left_motor.setVelocity(speed)
        right_motor.setVelocity(speed)