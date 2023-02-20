# robot class 
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c

class ROBOT:
    def __init__(self):
        self.sensors= {}
        self.motors = {}