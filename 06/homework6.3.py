a = int(input("Введите целое число: "))
while a > 9:
    digits = []
    while a > 0:
        digits.append(a % 10)
        a //= 10

    b = 1
    for digit in digits:
        b = b * digit

    a = b

print(a)