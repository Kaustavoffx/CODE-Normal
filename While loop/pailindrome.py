n = int(input('enter the number:'))
m = n
rev_no = 0

while n > 0:
    r = n % 10
    rev_no = 10 * rev_no + r
    n = n // 10

if m == rev_no:
    print('the number is palindrome')
else:
    print('the number is not palindrome')
