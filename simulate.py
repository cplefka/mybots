import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data
import numpy
import random
import constants as c 
from simulation import SIMULATION

simulation = SIMULATION()
simulation.Run()


""" 
numsArray = 2*c.PI*(numpy.arange(c.STEPS) / c.STEPS)
targetAngles = (c.PI/4)*numpy.sin(numsArray)


targetAnglesF = c.amplitudeF * numpy.sin(c.frequencyF * numsArray +c.phaseOffsetF)
targetAnglesB = c.amplitudeB * numpy.sin(c.frequencyB * numsArray +c.phaseOffsetB)

for i in range(0,c.STEPS):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_BackLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = targetAnglesF[i],
    maxForce = 500)
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robotId,
    jointName = b'Torso_FrontLeg',
    controlMode = p.POSITION_CONTROL,
    targetPosition = targetAnglesB[i],
    maxForce = 500)
    time.sleep(1/240)
p.disconnect()
#print(backLegSensorValues)
numpy.save("data/frontLegSensorValues.npy", frontLegSensorValues)
numpy.save("data/backLegSensorValues.npy", backLegSensorValues)
numpy.save("data/targetAngles.npy", targetAngles)
numpy.save("data/targetAnglesF.npy", targetAnglesF)
numpy.save("data/targetAnglesB.npy", targetAnglesB) """