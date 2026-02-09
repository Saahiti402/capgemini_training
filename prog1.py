n = int(input("Enter size of square matrix: "))
matrix = [list(map(int, input().split())) for _ in range(n)]

for row in matrix:
    row.reverse()          
    for i in range(n):
        row[i] ^= 1        

for row in matrix:
    print(row)   