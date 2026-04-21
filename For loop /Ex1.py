# Program to find the numbers those are not
# present in the range
list1 = [2, 5, 6, 7, 9, 11, 15]
valid_range = range(0, 10)
for a in list1:
    if a not in valid_range:
        print(f"{a} is not in the valid range.")
