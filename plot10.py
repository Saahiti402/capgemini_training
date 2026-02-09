import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="dark")
fmri=sns.load_dataset("fmri")
sns.lineplot(x="timepoint", y="signal", hue="region", style="event", data = fmri)
plt.show()   
