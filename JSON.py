import json

# some JSON:
x =  '{ "name":"Dev", "age":20, "city":"Ahmedabad"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["name"])
print(y["age"])
print(y["city"])
