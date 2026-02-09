n = int(input().strip())
arr = list(map(int, input().split()))

arr.sort()
x = arr[-2] if n > 1 else arr[0]
y = arr[-1]

avg = (x + y) / 2

result_sum = sum(v for v in arr if v >= avg)

print(result_sum)
