import matplotlib.pyplot as plt, numpy as np
from ex1 import computeCost,setup
X,y=setup()
theta0_vals = np.linspace(-10, 10, 100);
theta1_vals = np.linspace(-1, 4, 100);
Jval=np.zeros(shape=[100,100])
for i in range(100):
    for j in range(100):
        Jval[i,j]=computeCost(X,y,[theta0_vals[i],theta1_vals[j]])
fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")
ax.plot_surface(theta0_vals,theta1_vals,Jval)
plt.show()