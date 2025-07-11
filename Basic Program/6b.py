def find_largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

my_list = [4, 6, 8, 2, 1, 9, 5]
largest_number = find_largest_number(my_list)
print("The largest number in the list is:", largest_number)
