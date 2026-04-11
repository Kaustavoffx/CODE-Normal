# python program to check whether an input number
# is Armstrong or not using while loop
n = int(input("Enter the number"))
m = n
cube_sum = 0

while n != 0:
    r = n % 10
    cube_sum = cube_sum + r*r*r
    n = n // 10

if m == cube_sum:
    print('the number is Armstrong')
else:
    print('the number is not Armstrong')
