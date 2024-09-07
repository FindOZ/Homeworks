def generate_cube_numbers(limit):
    num = 2
    while True:
        cube = num ** 3
        if cube >= limit:
            return
        yield cube
        num += 1

limit = int(input("Введіть межу для кубів чисел: "))

cubes = generate_cube_numbers(limit)

for cube in cubes:
    print(cube)