def is_power(a, b):
     if a < b: 
         return False # prevent recursion
     if a == b:  
         return True  # prevent recursion
     else:
         return is_power(a / b, b) # recursion!