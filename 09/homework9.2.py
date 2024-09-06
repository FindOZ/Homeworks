
user_input = input("Введіть числа через кому: ")

numbers = [float(num) for num in user_input.split(',')]
def difference(*args):
    if not args:
        return 0

    diff = max(args) - min(args)

    return round(diff, 2)

print("Різниця між максимальним і мінімальним значенням:", difference(*numbers))