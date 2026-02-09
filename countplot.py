import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
sns.countplot(x="sex", data=tips)
plt.title("Count of Gender in Dataset")
plt.show()   

