# robot class 
import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, solutionID):
        self.robotId = p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain" + solutionID + ".nndf")
        os.system("rm brain" + solutionID + ".nndf")

    def Prepare_To_Sense(self):
        self.sensors= {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName)

    def Sense(self, t):
        for i in self.sensors: 
            self.sensors[i].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors = {}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
        for neuronN in self.nn.Get_Neuron_Names():
            if self.nn.Is_Motor_Neuron(neuronN):
                jointName = self.nn.Get_Motor_Neurons_Joint(neuronN)
                desiredAngle = self.nn.Get_Value_Of(neuronN)
        
                self.motors[jointName].Set_Value(self.robotId, desiredAngle)
       
        #for i in self.motors:
                    #self.motors[i].Set_Value(self.robotId, desiredAngle)

        #for i in self.motors:
            #self.motors[i].Set_Value(self.robotId, t)
    
    def Think(self):
        #self.nn.Print()
        self.nn.Update() 


    def Get_Fitness(self, solutionID): 
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        positionOfLinkZero = stateOfLinkZero[0]
        xCoordindateOfLinkZero = positionOfLinkZero[0]
        file = open("tmp" + solutionID + ".txt", "w")
        file.write(str(xCoordindateOfLinkZero))
        file.close()
        os.system("mv tmp"+ str(solutionID) + ".txt" + " fitness" + str(solutionID)+ ".txt")
