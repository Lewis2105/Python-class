def get_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

input_list = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in input_list] 

even_numbers = get_even_numbers(numbers)
print("Even numbers:", even_numbers)
