marks = int(input("Enter marks: "))

if marks >= 80 and marks <= 100:
    print("Grade A+")
elif marks >= 60 and marks < 80:
    print("Grade A")
elif marks >= 45 and marks < 60:
    print("Grade B")
elif marks >= 30 and marks < 45:
    print("Grade C")
elif marks < 30:
    print("Grade D")
else:
    print("Invalid marks! Please enter valid marks between 0 and 100.")
