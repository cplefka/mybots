#motor class 
import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
import numpy
import constants as c

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        self.motorValues = numpy.zeros(c.STEPS)
        self.Prepare_To_Act()


    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.phaseOffset = c.phaseOffset
        self.frequency = c.frequency
        name = str(self.jointName)

        if ("Front" in name): 
            self.frequency = self.frequency/2

        self.numsArray = 2*c.PI*(numpy.arange(c.STEPS) / c.STEPS)
        self.motorValues = self.amplitude*numpy.sin(self.frequency * self.numsArray + self.phaseOffset)

    def Set_Value(self, robotId, desiredAngle): 
        pyrosim.Set_Motor_For_Joint(
            bodyIndex = robotId,
            jointName = self.jointName,
            controlMode = p.POSITION_CONTROL,
            targetPosition = desiredAngle,
            maxForce = 500)
        
    def Save_Values(self):
        numpy.save("data/" + self.jointName + "MotorValues.npy", self.motorValues)
        