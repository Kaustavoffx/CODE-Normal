# --- Basic List Creation ---
emptyList = []
stringList = ["apple", "orange", "banana", "cherry"]
numberList = [10, 20, 30, 40, 50]
mixedList = [10, 2+5j, 30, "No", 40, 5.75, True]

# --- List Comprehension ---
numbers = [x for x in range(1, 11)]
evenNumbers = [x for x in range(1, 11) if x%2 == 0]

# --- Using list() constructor ---
myString = "Python3.12"
charList = list(myString)
myTuple = (1, 2, 3, 4, 5)
tupleList = list(myTuple)

# --- List evaluation from string ---
userInput = "[10, 20, 30]"
evalList = eval(userInput)

# --- List creation from user data (Script) ---
num = int(input("How many integers you want to insert? "))
user_numbers = []
for i in range(num):
    val = int(input(f"Enter integer {i+1}: "))
    user_numbers.append(val)
print("The list of numbers is: ", user_numbers)