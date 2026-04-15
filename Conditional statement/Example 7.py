#Program to calculate positive difference of two
#numbers
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
result=0
if x>y:
    result=x-y
else:
    result=y-x
print("the difference of", x, "and", y, "is", result)