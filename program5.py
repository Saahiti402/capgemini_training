n = int(input("Size of the array:"))
product = 1
A = list(map(int, input().split()))
for i in A:
    if i % 7 == 0:
        product *= i
        
print(product)