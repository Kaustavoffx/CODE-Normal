#factorial
n=int(input("Enter a number:"))
f=1
for i in range (1,n+1):
    f*=i
print("factorial of ",n, "is", f)

#output
# Enter a number:5
# factorial of  5 is 120