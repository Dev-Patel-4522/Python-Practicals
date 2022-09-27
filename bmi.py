##
#Python's program to calculate the body mass index (BMI) of an individual
##

#Define the constants
METER   = 100

#Read the inputs from user
height  = float(input("Enter your height in Centimeters: "))
weight  = float(input("Enter your weight in Kg: "))

temp    = height / METER
#Calculate the BMI
bmi = weight / (temp*temp)

#Display the result
print("Your Body Mass Index is: ","%d"%(bmi))
