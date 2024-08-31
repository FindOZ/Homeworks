
def add_one():
    digits_input = input("Напишіть цифри: ")
    digits = [int(digit) for digit in digits_input.split()]
    number = int(''.join(map(str, digits)))
    number += 1
    result = [int(char) for char in str(number)]
    return result
result = add_one()
print(result)


# digits = [1, 2, 3, 4]
# result = add_one(digits)
# print(result)