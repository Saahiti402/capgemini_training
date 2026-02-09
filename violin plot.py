import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
plt.title("violin plot of total bill by day and gender")
plt.show()   



