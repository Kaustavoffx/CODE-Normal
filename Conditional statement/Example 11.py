num1=int(input("Enter the dividend:"))
num2=int(input("Enter the divisor:"))
if num2==0:
    print("Division by zero is not allowed.")
elif num1%num2==0:
    print(num1,"is divisible by", num2)
else:
    print(num1,"is not divisible by", num2)