numbers = input("Enter comma seprated values: ")

numbers_list = numbers.split(",")
numbers_tuple = tuple(numbers_list)

print(f"List: {numbers_list}")
print(f"Tuple: {numbers_tuple}")