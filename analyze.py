import numpy
import matplotlib.pyplot

backLegSensorVals = numpy.load("data/backLegSensorValues.npy")
frontLegSensorVals = numpy.load("data/frontLegSensorValues.npy")


matplotlib.pyplot.plot(backLegSensorVals)
matplotlib.pyplot.plot(frontLegSensorVals)
matplotlib.pyplot.show()