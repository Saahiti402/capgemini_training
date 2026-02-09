import seaborn as sns
import matplotlib.pyplot as plt
x = ['sun', 'mon', 'fri', 'sat', 'tue', 'wed', 'thu']
y = [5, 6.7, 4, 6, 2, 4.9, 1.8]
ax = sns.stripplot(x=x, y=y)
ax.set(xlabel = 'Days', ylabel='Amount Spent')
plt.title('Daily Spending (Custom Data)')
plt.show()   
