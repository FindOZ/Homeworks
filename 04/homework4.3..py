import random

print( "LIST START" )
a = random.randint(1, 100)
b = [random.randint(3, 10) for b in range(a)]
print(b)
c = b.pop(0)
d = b.pop(1)
e = b.pop(-2)
f = [c, d, e]
print(f)
print( "LIST END" )