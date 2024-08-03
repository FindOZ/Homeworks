a = [2, 1, 0, 0, 3]
a.count(0)
x = a.count(0)
while 0 in a:
    a.remove(0)
a.extend([0] * x)
print(a)
a = [0]
a.count(0)
b = a.count(0)
while 0 in a:
    a.remove(0)
a.extend([0] * b)
print(a)
a = [2, 1, 0, 0, 3]
a.count(0)
x = a.count(0)
while 0 in a:
    a.remove(0)
a.extend([0] * x)
print(a)
a = [1, 0, 13, 0, 0, 0, 5]
a.count(0)
x = a.count(0)
while 0 in a:
    a.remove(0)
a.extend([0] * x)
print(a)
a = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
a.count(0)
x = a.count(0)
while 0 in a:
    a.remove(0)
a.extend([0] * x)
print(a)



# while
# a = (c for c)
# a.remove(0)
# print(b)
# print(a)
# for a in range(b):
#     a.append(0)
# print(a[-1::-1])

# print
# print(a.index (0))
# b = [0, 1, 0, 12, 3]
# b.sort()
# print(b[-1::-1])
