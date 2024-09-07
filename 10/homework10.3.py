def is_even(number):
    return number % 2 == 0

input_number = int(input("Введіть ціле число: "))

if is_even(input_number):
    print("Число парне.")
else:
    print("Число непарне.")