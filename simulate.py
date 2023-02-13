import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data
import numpy
import random 

pi = numpy.pi
STEPS = 500


physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-90.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")

p.loadSDF("world.sdf") 
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(STEPS)
frontLegSensorValues = numpy.zeros(STEPS)

numsArray = 2*pi*(numpy.arange(STEPS) / STEPS)
targetAngles = (pi/4)*numpy.sin(numsArray)

amplitudeF = pi/4
frequencyF = 3 
phaseOffsetF = 0

amplitudeB = pi/4
frequencyB = 3 
phaseOffsetB = pi/4

targetAnglesF = amplitudeF * numpy.sin(frequencyF * numsArray +phaseOffsetF)
targetAnglesB = amplitudeB * numpy.sin(frequencyB * numsArray +phaseOffsetB)

for i in range(0,STEPS):
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
numpy.save("data/targetAnglesB.npy", targetAnglesB)