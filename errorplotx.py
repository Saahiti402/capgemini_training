import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7]
y = [1,2,1,2,1,2,1]
x_error = 0.5
plt.errorbar(x, y, xerr=x_error, fmt='o')
plt.show()   
