import numpy 
import matplotlib.pyplot as plt
from numpy import diff
import os
a= numpy.loadtxt('samples/1.raw', skiprows=1, delimiter=",")

plt.plot(a[:,0], a[:,1])
plt.title("Youngs Modulus of Sample")
plt.show()
