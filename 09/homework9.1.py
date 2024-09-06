
user_text = input("Введіть текст: ")

user_words = input("Введіть слова для пошуку, розділяючи комами: ").split(',')
def pop_words(text: str, words: list) -> dict:
    text = text.lower()

    word_list = text.split()

    word_count = {word: 0 for word in words}

    for word in words:
        word_count[word] = word_list.count(word)

    return word_count

result = pop_words(user_text, [word.strip().lower() for word in user_words])

print(result)