N = int(input("Enter a positive integer N: "))
sum_of_squares = sum(i**2 for i in range(1, N + 1))

print(f"The sum of squares from 1 to {N} is: {sum_of_squares}")