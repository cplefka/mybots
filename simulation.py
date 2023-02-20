#simulation class 
from robot import ROBOT
from world import WORLD
from motor import MOTOR 
from sensor import SENSOR

import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import time
import constants as c

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.configureDebugVisualizer(p.COV_ENABLE_GUI,0) 
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.GRAV)    
        
        self.world = WORLD() 
        self.robot = ROBOT()

