
import string

a = input("Введите две буквы через дефис: ")

start_letter, end_letter = a.split('-')

start_index = string.ascii_letters.index(start_letter)
end_index = string.ascii_letters.index(end_letter)

missed_letters = string.ascii_letters[start_index:end_index + 1]

print(missed_letters)


