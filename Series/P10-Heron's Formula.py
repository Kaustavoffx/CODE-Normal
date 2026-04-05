a = float(input("Enter the length of first side of the triangle: "))
b = float(input("Enter the length of second side of the triangle: "))
c = float(input("Enter the length of third side of the triangle: "))

s = (a + b + c) / 2

# Area of the triangle using Heron's formula (Added the square root ** 0.5)
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(f"Area of the triangle: {area} unit²")

# Corrected Output for 7, 8, 9:
# Area of the triangle: 26.832815729997476 unit²