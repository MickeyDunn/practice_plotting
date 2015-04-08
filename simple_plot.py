import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname="inflammation.csv", delimiter=',')
print data
print 'data dimensions', data.shape

fig = plt.figure(figsize=(10.,3.))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(data.mean(axis=0))

axes2.set_ylabel('max')
axes2.plot(data.max(axis=0))

axes3.plot(data.min(axis=0))
axes3.set_ylabel('min')

plt.show()