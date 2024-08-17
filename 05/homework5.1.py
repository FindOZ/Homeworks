
import keyword
import string

a = str(input("Input a "))

if a in keyword.kwlist:
  print(False)

elif a[0].isdigit():
    print(False)

elif a.count("_") > 1:
    print(False)
elif " " in a:
    print(False)

elif any(char.isupper() for char in a):
    print(False)

elif any(char in (set(string.punctuation) - {"_"}) for char in a):
    print(False)

else:
    print(True)