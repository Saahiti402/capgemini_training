def sum_array(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + sum_array(arr, n-1)
n = int(input("Enter size of list:"))
arr = list(map(int,input("Enter the elements : ").split()))
print(sum_array(arr, n))