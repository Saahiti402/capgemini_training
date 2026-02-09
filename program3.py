n = int(input("Enter the number of kilometers:"))
sum = 0
for i in range (n+1):
    if i %2==0:
        sum+=i
        
print(sum)