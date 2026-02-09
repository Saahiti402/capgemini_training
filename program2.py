A = list(map(int, input().split()))
count = 0

for i in A:
    if i == 0:
        count += 1

print(count)   