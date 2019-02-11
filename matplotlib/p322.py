import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

x=np.linspace(0,2*np.pi)
y=np.sin(x)

#データx,yをグラフにプロットし、表示してください
x=np.linspace(0,2*np.pi)
y=np.sin(x)

plt.plot(x,y)
plt.show()
