P = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest (as a percentage): "))
n = int(input("Enter the number of years: "))

A = P * (1 + r / 100) ** n

CI = A - P

print(f"The compound interest is: {CI:.2f}")