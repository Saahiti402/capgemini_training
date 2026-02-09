def longest_common_substring_ascii_sum(S1, S2):
    m, n = len(S1), len(S2)
    max_len = 0
    ending_index_s1 = 0 

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S1[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    ending_index_s1 = i
    
    if max_len == 0:
        return 0

    start = ending_index_s1 - max_len
    longest_substring = S1[start:ending_index_s1]

    return sum(ord(c) for c in longest_substring)

S1, S2 = input().split()

print(longest_common_substring_ascii_sum(S1, S2))   