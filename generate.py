import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1

x = 0
y = 0
z = .5

pyrosim.Start_SDF("boxes.sdf")

for a in range(5):
    for b in range(5):
        length = 1
        width = 1
        height = 1
        for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x+a,y+b,z+i] , size=[length, width, height])
            length = length * .9
            width = width * .9
            height = height * .9

pyrosim.End()