n = int(input("Enter number: "))
pos = int(input("Enter position: "))

n = abs(n)

for i in range(1, pos):
    n //= 10

if n == 0:
    print(-1)
else:
    print(n % 10)