#simulation class 
from robot import ROBOT
from world import WORLD
from motor import MOTOR 
from sensor import SENSOR

class SIMULATION:
    def __init__(self):
        self.world = WORLD() 
        self.robot = ROBOT()

