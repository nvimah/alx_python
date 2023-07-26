def fibonacci_sequence(n):
     if n in {0, 1}:
       return    fibonacci_sequence(n-1) + fibonacci_sequence(n -2)
