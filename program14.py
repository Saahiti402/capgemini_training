n = int(input("Enter the size of the array : "))
if n == 0:
    print(-1)
else:
    files = input("Enter names of files : ").split()
    m = -1
    for f in files:
        if f.startswith("File_") and f[5:].isdigit():
            m = max(m, int(f[5:]))
    print(m)