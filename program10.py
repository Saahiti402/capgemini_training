n = int(input("Enter number of problems: "))
p = int(input("Enter number of minutes: "))

total_time = 240
available_time = total_time - p  
time_used = 0
count = 0

for i in range(1, n + 1):
    time_required = 5 * i
    if time_used + time_required <= available_time:
        time_used += time_required
        count += 1
    else:
        break

print(count)   