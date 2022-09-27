# Collect input from the user
kilometers = float(input('How many kilometers?: '))
miles1 = float(input("Enter the value in miles: "))
# conversion factor
conv_fac = 0.621371
conversion_factor = 1.60934
# calculating miles to kilometers
miles = kilometers * conv_fac
# calculating kilometers to miles
kilometers1 = miles1 * conversion_factor
# print the statement
print('%0.4f Kilo Meters =  %0.4f Miles' %(kilometers,miles))
print('%0.4f Miles = %0.4f Kilo Meters' %(miles1, kilometers1))
