def correct_sentence():
    sentence1 = input("Напишіть перше речення: ")
    sentence2 = input("Напишіть друге речення: ")
    def fix_sentence(sentence):
        sentence = sentence.capitalize()
        if not sentence.endswith('.'):
            sentence += '.'
        return sentence
    sentence1_fixed = fix_sentence(sentence1)
    sentence2_fixed = fix_sentence(sentence2)
    return f"{sentence1_fixed} {sentence2_fixed}"
a = correct_sentence()
print(a)