# --- List creation from user data (Script) ---
num = int(input("How many integers you want to insert? "))
user_numbers = []
for i in range(num):
    val = int(input(f"Enter integer {i+1}: "))
    user_numbers.append(val)
print("The list of numbers is: ", user_numbers)