def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_generator(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

upper_limit = int(input("Введіть верхню межу генератора простих чисел: "))

print(f"Прості числа до {upper_limit}:")
for prime in prime_generator(upper_limit):
    print(prime)