#motor class 
import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import numpy
import constants as c

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        MOTOR.Prepare_To_Act(self)


    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.phaseOffset = c.phaseOffset
        self.frequency = c.frequency

        self.numsArray = 2*c.PI*(numpy.arange(c.runs) / c.runs)
        self.motorValues = self.amplitude*numpy.sin(self.frequency * self.numsArray + self.offset)

    def Set_Value(self, robotId, t): 
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = self.motorValues[t],
            maxForce = 500)
        