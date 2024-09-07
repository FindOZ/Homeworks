def custom_sequence(first_member, n, func):
    count = 0
    current_value = first_member
    while count < n:
        yield current_value
        current_value = func(current_value)
        count += 1

def square(x):
    return x ** 2

first_member = int(input("Введіть перше число послідовності: "))
n = int(input("Введіть кількість членів послідовності: "))

print("Умова послідовності: ввиведення у 2 ступінь.")
sequence = custom_sequence(first_member, n, square)

print(f"Послідовність з {n} членів:")
for value in sequence:
    print(value)
