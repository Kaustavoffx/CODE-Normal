#pythone program to print reverse number n=int(input('enter the number'))
n=int(input("Enter the number: "))
rev_no=0
while n!=0:
    r=n%10
    rev_no=10*rev_no+r
    n=n//10
print('the reverse number=',rev_no)