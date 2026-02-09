n = int(input("Enter the size of team : "))
names = input("Enter names : ").split()
ans = ""
for name in names:
    ans += name[0]
print(ans)