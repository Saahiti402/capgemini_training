import matplotlib.pyplot as plt
import numpy as np
data = np.random.randn(1000)
plt.hist(data, bins=30, color ='skyblue', edgecolor='black')
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title('Basic Histogram')

plt.show()
