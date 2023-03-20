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
    def __init__(self, directOrGUI):
        directOrGUI= str(directOrGUI)
        if directOrGUI=="DIRECT":
            self.physicsClient = p.connect(p.DIRECT) 
            c.sleep = 1/10000000000
        elif directOrGUI == "GUI":
            self.physicsClient = p.connect(p.GUI)
            p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
            c.sleep = 1/1000
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.GRAV)    

        self.world = WORLD() 
        self.robot = ROBOT()
        self.directOrGUI = directOrGUI 


    def Run(self): 
        for t in range(0,c.STEPS):
            #print(t)
            time.sleep(c.sleep)
            p.stepSimulation()
            self.robot.Sense(t) 
            self.robot.Think()
            self.robot.Act(t) 

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        p.disconnect()

