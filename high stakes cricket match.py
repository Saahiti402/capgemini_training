list = []
list.append(95.0)
n = int(input("Enter number of overs: "))
for i in range(1,n):
    list.append(list[i-1]+20.5)
    
print(list)