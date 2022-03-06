def find_sum_of_numbers_count_of_numbers_divisibleby(number):
    numbers_divisible_by_number = [num for num in range(1, 101) if num % int(number) == 0]
    sum_of_numbers = sum(numbers_divisible_by_number)
    count_of_numbers = sum(1 for _ in numbers_divisible_by_number)
    return sum_of_numbers, count_of_numbers


print(type(find_sum_of_numbers_count_of_numbers_divisibleby(5)))
