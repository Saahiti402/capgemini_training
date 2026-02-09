import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="white")
rs = np.random.RandomState(10)
d = rs.normal(size=100)
sns.histplot(d, kde=True, color="m")
plt.show()   