def minimize_sum(n, arr):
    min_sum = float('inf')
    
    for i in range(n):
        for j in range(i + 1, n):
            avg = (arr[i] + arr[j]) / 2.0
            current_sum = 0
            for x in arr:
                if x >= avg:
                    current_sum += x
            min_sum = min(min_sum, current_sum)
    
    return min_sum

n = int(input())
arr = list(map(int, input().split()))

print(int(minimize_sum(n, arr)))   