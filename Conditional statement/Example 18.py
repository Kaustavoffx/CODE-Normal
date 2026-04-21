n1 = float(input("Enter number 1: "))
n2 = float(input("Enter number 2: "))
op = input("Enter an operator (+, -, *, /) : ")

if op == '+':
    result = n1 + n2
    print("Result:", result)
elif op == '-':
    result = n1 - n2
    print("Result:", result)
elif op == '*':
    result = n1 * n2
    print("Result:", result)
elif op == '/':
    if n2 != 0:
        result = n1 / n2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed. Program Terminated")
else:
    print("Invalid operator entered.")
