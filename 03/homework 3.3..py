print( "LIST START" )

print("Enter the list")
number_1 = []
number_1 = input().split()
print(number_1)
a = len (number_1) // 2
if a % 2 != 1:
   a = a + 1
number_2 = number_1[:a]
number_3 = number_1[a:]
print(number_2)
print(number_3)

number_4 = number_2 + number_3
print(number_4)
print( "LIST END" )