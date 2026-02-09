n = int(input())
votes = list(map(int, input().split()))
freq = {}
for v in votes:
    freq[v] = freq.get(v, 0) + 1
majority = n // 2
winner = -1
for party, count in freq.items():
    if count > majority:
        winner = party
        break

print(winner)   