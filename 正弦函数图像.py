import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(8,5), dpi=80)

plt.xlabel("t")
plt.ylabel("x(t)")
ax = plt.subplot(111)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

x = np.arange(-2*np.pi, 2*np.pi, 0.1 )
y1=np.cos(x)
y2=np.sin(x)

plt.plot(x, y1)
plt.plot(x, y2)

plt.show()