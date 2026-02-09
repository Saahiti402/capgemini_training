def min_steps_magic_string(S):
    if len(set(S)) == 1:
        return 0 
    freq = {}
    for char in S:
        freq[char] = freq.get(char, 0) + 1
    max_freq = max(freq.values())
    return len(S) - max_freq

S = input().strip()
print(min_steps_magic_string(S))   