num = int(input("Enter a number from 0 to 50: "))
if num >= 0 and num < 10:
    print("Number is in the range 0 to 10.")
elif num >= 10 and num < 20:
    print("Number is in the range 10 to 20.")
elif num >= 20 and num < 30:
    print("Number is in the range 20 to 30.")
elif num >= 30 and num < 40:
    print("Number is in the range 30 to 40.")
elif num >= 40 and num <= 50:
    print("Number is in the range 40 to 50.")
else:
    print("Number is out of the given range.")