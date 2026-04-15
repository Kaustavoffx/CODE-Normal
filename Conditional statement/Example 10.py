num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
num3=float(input("Enter third number:"))
max=num1
if num2>max:
    max=num2
if num3>max:
    max=num3
print("The largest number is:",max)