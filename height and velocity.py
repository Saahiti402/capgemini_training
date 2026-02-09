H = int(input("Enter the height : "))
V = int(input("Enter the initial velocity : " ))
Vn =int (input("Enter the Vn : "))
e = V//Vn
rebound_height = H*(e**2)
print(rebound_height)