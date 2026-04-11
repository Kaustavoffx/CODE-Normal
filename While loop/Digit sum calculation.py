n=int(input('Enter the numbers :'))
sum=0
while n!=0:
    r=n%10
    sum=sum+r
    n=n//10
print('The sum of digits=', sum)