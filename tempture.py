fahrenheit1 = float(input("Enter temperature in fahrenheit: "))
celsius = float(input("Enter temperature in celsius: "))

celsius1 = (fahrenheit1 - 32) * 5/9
fahrenheit = (celsius * 9/5) + 32

print('%.2f Fahrenheit is: %0.2f Celsius' %(fahrenheit1, celsius1))
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))
