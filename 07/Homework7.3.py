def second_index(text, some_str):
    first_occurrence = text.find(some_str)

    if first_occurrence == -1:
        return None
    second_occurrence = text.find(some_str, first_occurrence + 1)

    if second_occurrence != -1:
        return second_occurrence

    return None

text = input("Напишіть текст: ")
some_str = input("Напишіть символ для пошуку: ")

result = second_index(text, some_str)

if result is not None:
    print(f"Друге входження символу '{some_str}' під індексом: {result}")
else:
    print(f"Друге входження '{some_str}' не знайдено.")