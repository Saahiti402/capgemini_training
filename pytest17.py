import unittest
a = int(input())
result = []

for i in range(a):
    var = list(map(int, input().split()))
    result.append(var)

for o in range(a):
    result[o] = result[o][::-1]

for j in range(a):
    for g in range(len(result[j])):
        if result[j][g] == 0:
            result[j][g] = 1
        else:
            result[j][g] = 0

for row in result:
    for val in row:
        print(val, end="")
    print()

