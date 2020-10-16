import numpy as np
import matplotlib.pyplot as plt

def x(t):
      return np.exp(-1*t)*np.cos(8*t)



t=np.arange(-15,15,0.01)
plt.plot(t,x(t),'r-')
plt.show()