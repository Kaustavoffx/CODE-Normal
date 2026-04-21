Ch = input("Enter a Character or number:")
if Ch >= 'a' and Ch <= 'z':
    print("Lower case character")
elif Ch >= 'A' and Ch <= 'Z':
    print("Upper case character")
elif Ch >= '0' and Ch <= '9':
    if int(Ch) % 2 == 0: 
        print("An even number")
    else:
        print("An odd number")
