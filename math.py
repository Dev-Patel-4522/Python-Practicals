# Python program to calculate square root

import math

# Declare value to calculate square root
val = float(input('Number?: '))

if val > 0:

    # Calculate square root using sqrt() method
    sqr = math.sqrt(val)
    print("Square Root of ", val,"is: ",sqr)
else:
    print("Please give value greater then 0");


val2 = int(input('Number?: '))

if val2 > 0:

    # Calculate square root using sqrt() method
    sqr2 = math.sqrt(val2)
    print("Square Root of ", val2,"is: ",sqr2)
else:
    print("Please give value greater then 0");
