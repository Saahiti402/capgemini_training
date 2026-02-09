def rebound_height(H, V, Vn):
    return int(H * (V / Vn) ** 2)

H, V, Vn = map(int, input().split())

print(rebound_height(H, V, Vn))   