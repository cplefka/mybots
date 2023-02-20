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

    def Run(self): 
        for i in range(0,c.STEPS):
            # p.stepSimulation()
            # backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
            # frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex = robotId,
            # jointName = b'Torso_BackLeg',
            # controlMode = p.POSITION_CONTROL,
            # targetPosition = targetAnglesF[i],
            # maxForce = 500)
            # pyrosim.Set_Motor_For_Joint(
            # bodyIndex = robotId,
            # jointName = b'Torso_FrontLeg',
            # controlMode = p.POSITION_CONTROL,
            # targetPosition = targetAnglesB[i],
            # maxForce = 500)
            print(i)
            time.sleep(1/60)
    
    def __del__(self):
        p.disconnect()

