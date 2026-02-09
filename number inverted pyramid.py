n = int(input("Enter n : "))
num = n * (n + 1) // 2
for i in range(n, 0, -1):
    line = []
    for j in range(i):
        line.append(str(num))
        num -= 1
    print("*".join(line))