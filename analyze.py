import numpy
import matplotlib.pyplot

backLegSensorVals = numpy.load("data/backLegSensorValues.npy")
frontLegSensorVals = numpy.load("data/frontLegSensorValues.npy")
targetVals = numpy.load("data/targetAngles.npy")
targetValsF = numpy.load("data/targetAnglesF.npy")
targetValsB = numpy.load("data/targetAnglesB.npy")

#matplotlib.pyplot.plot(backLegSensorVals, label='Back Leg', linewidth = 5, color = "pink")
#matplotlib.pyplot.plot(frontLegSensorVals, label='Front Leg', color = "green")
#matplotlib.pyplot.legend()
#matplotlib.pyplot.plot(targetVals)

matplotlib.pyplot.plot(targetValsB, label='Back Leg', linewidth = 5, color = "pink")
matplotlib.pyplot.plot(targetValsF, label='Front Leg', color = "green")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()