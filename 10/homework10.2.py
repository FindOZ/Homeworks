def first_word(text):
    text = text.lstrip(' ,.')
    word = ''
    for char in text:
        if char.isalpha() or char == "'":
            word += char
        elif word:
            break

    return word

input_text = input("Введіть рядок: ")
print("Перше слово в рядку:", first_word(input_text))