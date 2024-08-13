a = int(input("Enter the first number: "))
b = int(input("Enter the second number :"))

a, b = b, a + 1
print(f"After swapping, first number: {a}, second number: {b}")