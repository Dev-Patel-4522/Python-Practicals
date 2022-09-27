# Program to find Area of Circle using Circumference

# Taking circumference  from user
circumference  = float(input("Enter the circumference  of circle : "))

# Taking circumference  measure unit from user
unit = input("Enter the measure unit of circumference  (e.g. in, cm) : ")

# Finding area of a circle using ( A = 1/4 * /\ * D*D ) formula
area = ((circumference  * circumference ) / (4 * (22 / 7) ))

# Printing the area
print("Area of circle is : ",area,unit+"2")
