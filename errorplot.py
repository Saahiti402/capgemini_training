import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7]
y = [1,2,1,2,1,2,1]
y_error = 0.2
plt.errorbar(x, y, yerr=y_error, fmt='-o')
plt.show()   