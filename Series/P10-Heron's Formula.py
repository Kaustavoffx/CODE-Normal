a=float(input("Enter the length of first side of the triangle: "))
b=float(input("Enter the length of second side of the triangle: "))
c=float(input("Enter the length of third side of the triangle: "))

s=(a+b+c) /2

#Area of the triangle using Heron's formula
area =(s* (s-a)*(s-b)*(s-c))

print(f"Area of the triangle: {area} unit²")

#output
# Enter the length of first side of the triangle: 7
# Enter the length of second side of the triangle: 8
# Enter the length of third side of the triangle: 9
# Area of the triangle: 720.0 unit²