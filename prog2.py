n = int(input("Enter number of houses: "))
A = list(map(int, input("Enter stairs in each house: ").split()))

count = 0

for stairs in A:
    if stairs % 3 == 0:
        count += 1

print(count)