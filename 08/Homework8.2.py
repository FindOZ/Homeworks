import string
user_input = input("Введіть строку для перевірки, чи є вона паліндромом: ")
def is_palindrome(s):
    s = s.lower()
    s = ''.join(char for char in s if char.isalnum())
    return s == s[::-1]

result = is_palindrome(user_input)
print(result)