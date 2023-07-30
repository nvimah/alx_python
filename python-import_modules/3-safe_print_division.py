a = 10
b = 0
def safe_print_division(a, b):
  return a / b 
try:
   result = safe_print_division(a, b)
except ZeroDivisionError:
   print('None')
else:
  print("{} / {} = {}".format(a, b, result))
