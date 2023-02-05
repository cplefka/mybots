import numpy
import matplotlib.pyplot

backLegSensorVals = numpy.load("data/backLegSensorValues.npy")
frontLegSensorVals = numpy.load("data/frontLegSensorValues.npy")


matplotlib.pyplot.plot(backLegSensorVals, label='Back Leg', linewidth = 5, color = "pink")
matplotlib.pyplot.plot(frontLegSensorVals, label='Front Leg', color = "green")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()