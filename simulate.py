import pyrosim.pyrosim as pyrosim
import pybullet as p
import time
import pybullet_data
import numpy
import random
import constants as c 
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()


