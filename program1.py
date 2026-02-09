capacity = int(input("Enter the capacity of the ship: "))
people = int(input("Enter number of people: "))
count = 0
if people % capacity == 0:
    count = people // capacity  
else:
    count = people // capacity + 1
print(count)