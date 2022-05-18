from  vpython import *  # Import graphing features
from numpy import arange, cos, exp


funct1 = gcurve(color=color.cyan)  # A connected curve object


for x in arange(0., 8.1, 0.1):  # x goes from 0 to 8
    funct1.plot(pos=(x, 5. * cos(2. * x) * exp(-0.2 * x)))  # Plot