try:
  print(e)
except NameError:
  print("Variable e is not defined")
except:
  print("Something else went wrong")
