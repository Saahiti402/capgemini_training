list = []
list.append(4)
n = int(input("Enter value of n:"))
for i in range(1, n):
    list.append(i*i + list[i-1])
    
print(list)
    