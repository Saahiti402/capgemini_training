import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")
iris = sns.load_dataset("iris")
sns.swarmplot(x="species", y="sepal_length", data=iris)

plt.show()   
