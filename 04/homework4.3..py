import random

print( "LIST START" )
b = [random.randint(3, 10) for a in range(10)]
print(b)
c = b.pop(0)
d = b.pop(1)
e = b.pop(-2)
f = [c, d, e]
print(f)
print( "LIST END" )