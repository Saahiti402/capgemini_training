import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="dark")
fmri = sns.load_dataset("fmri")
sns.lmplot(x="timepoint", y="signal", hue="region", data=fmri)
plt.show()   