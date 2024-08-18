import string

a = str(input("Input a "))
b = ''
for char in a:
    if char not in string.punctuation:
            b += char

c = b.split()
d = []
for word in c:
    d.append(word.capitalize())
hashtag = '#' + ''.join(d)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print(hashtag)


