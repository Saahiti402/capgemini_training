import seaborn as sn
import matplotlib.pyplot as plt
plt.plot([0,1], [10, 11], label="Line 1")
plt.plot([0,1], [11, 10], label = "Line 2")
plt.scatter([0,1], [10.5, 10.5], color='blue', marker='o', label='Dots')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Simple line and Dot plot")
plt.legend()
plt.show()   




