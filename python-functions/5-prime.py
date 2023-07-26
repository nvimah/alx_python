def is_prime(number):
  if  number < 1 or number % 2 == 0 or number % 3 == 0 or number % 7 == 0:
   return False
  else:
    return True
print(is_prime(17))
print(is_prime(15))
print(is_prime(-5))
print(is_prime(0))