# Program to find Area of Circle using radius

# Taking radius from user
r = float(input("Enter the radious of circle : "))

# Taking radius measure unit from user
unit = input("Enter the measure unit of radius (e.g. in, cm) : ")

# Finding area of a circle using ( A = /\R*R ) formula
area = ((22/7) * (r*r))     #using 22/7
area1 = (3.14 * (r*r))    #using 3.14

# Print the area
print("Area of circle is : ",area,unit+"2")
print("Area of circle is : ",area1,unit+"2")
