
import string

a = input("Введите две буквы через дефис:")

start_letter, end_letter = a.split('-')

start_index = string.ascii_letters.index(start_letter)
end_index = string.ascii_letters.index(end_letter)
if start_index < end_index - 1:
    missed_letters = string.ascii_letters[start_index + 1:end_index]
else:
    missed_letters = ""

print(missed_letters)


