import numpy as np
import pyrosim.pyrosim as pyrosim
import random
import os

length = 1
width = 1
height = 1

class SOLUTION:
    def __init__(self):
        randWeight1 = np.random.rand()
        randWeight2 = np.random.rand()
        matrix = np.array([[randWeight1, randWeight2]])
        for i in range(2):
            randWeight1 = np.random.rand()
            randWeight2 = np.random.rand()
            add_row = np.array([[randWeight1, randWeight2]])
            matrix = np.concatenate((matrix, add_row), axis=0)
        self.weights = matrix
        self.weights = self.weights* 2 - 1

    def Evaluate(self, directOrGUI):
        self.Create_World()
        self.Generate_Body()
        self.Generate_Brain()
        os.system("python3 simulate.py " + directOrGUI )
        fitnessFile = open("fitness.txt", "r")
        self.fitness = float(fitnessFile.readline())
        fitnessFile.close()

    def Create_World(self): 
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[-3,3,.5] , size=[1,1,1]) 
        pyrosim.End()