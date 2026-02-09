n = int(input("Enter the size of the square matrix: "))
matrix = []

print("Enter the matrix row by row:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

is_upper = True
for i in range(1, n):
    for j in range(i):
        if matrix[i][j] != 0:
            is_upper = False
            break
    if not is_upper:
        break

print("Upper Triangular Matrix" if is_upper else "Not Upper Triangular Matrix")   