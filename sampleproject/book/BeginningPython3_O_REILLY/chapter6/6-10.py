class Laser():
    def does(self):
        return 'disintegrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.s_phone = SmartPhone()

    def does(self):
        return 'Robot.Laser does {}\nRobot.Claw does {}\nRobot.SmartPhone does {}'\
            .format(self.laser.does(), self.claw.does(), self.s_phone.does())

robot = Robot()
print(robot.does())