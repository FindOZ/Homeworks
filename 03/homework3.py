print( "CALCULATOR START" )

print("Enter first number")
number_1 = input()
number_1 = int(number_1)

print("Enter second number")
number_2 = input()
number_2 = int(number_2)

print ("Enter operation")
operation = input()
if operation == "+":
    print(number_1 + number_2)
elif operation == "-":
    print(number_1 - number_2)
elif operation == "*":
    print(number_1 * number_2)
elif operation == "/":
    if number_2 == 0:
        print("Error! Division by zero.")
    elif number_2 != 0:
        print(number_1 / number_2)
else:
      print("Invalid operation. Please enter one of +, -, *, /.")
print("CACLULATOR END")