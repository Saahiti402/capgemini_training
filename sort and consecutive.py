n = int(input("Enter the size : "))
m = list(map(int,input("Enter the elements : ").split()))
m.sort()
is_consecutive = 1
for i in range (n-1):
    if m[i+1] - m[i] != 1 :
        is_consecutive=0
        break
print(is_consecutive)