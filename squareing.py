# Python Program to Calculate Square of a Number using arithmetic opration

number = float(input(" Please Enter any numeric Value : "))

square = number * number  #Using Arithmetic opration

print("The Square of a Given Number {0}  = {1}".format(number, square))


# Python Program to Calculate Square of a Number using exponent

number1 = float(input(" Please Enter any numeric Value : "))

square1 = number1 ** 2  # Using Exponent

print("The Square of a Given Number {0}  = {1}".format(number1, square1))


# Python Program for Square of a Number using def

def square(num):  # Using def
    return num * num

number2 = float(input(" Please Enter any numeric Value : "))

square2 = square(number2)  #Using square function

print("The Square of a Given Number {0}  = {1}".format(number2, square2))
