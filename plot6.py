import matplotlib.pyplot as plt
import numpy as np
N=5
boys = (20, 35, 30, 35, 27)
girls = (25, 32, 34, 20, 25)
boyStd = (2, 3, 4, 1, 2)
girlStd = (3,5, 2, 3, 3)
ind = np.arange(N)
width = 0.35
fig=plt.subplots(figsize=(10, 7))
p1= plt.bar(ind, boys, width, yerr = boyStd)
p2= plt.bar(ind, girls, width, bottom = boys, yerr = girlStd)
plt.ylabel('Contribution')
plt.title('Contribution by the teams')
plt.xticks(ind, ('71', '12', '73', '74', '15'))
plt.yticks(np.arange(0, 81, 10))
plt.legend((p1[0], p2[0]), ('boys', 'girls'))
plt.show()