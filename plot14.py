import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="darkgrid")
x=[1, 2, 3, 4, 5]
y=[10, 12, 15, 18, 22]
plt.plot(x, y, marker='o', linestyle='-', color='blue', label="Trend")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Matplotlib Plot with Seaborn Theme")
plt.legend()
plt.show()