def find_unique_value(numbers):
    for num in numbers:
        if numbers.count(num) == 1:
            return num

user_input = input("Введіть числа чепез пробіл: ")

numbers = list(map(int, user_input.split()))

unique_value = find_unique_value(numbers)
print("Унікальне число:", unique_value)