# A simple Python function to demonstrate
# Polymorphism - means the same function name (but different signatures) being used for different types.
 
def add(x, y, z = 0):
    return x + y+z
 
# Driver code
print(add(2, 3))
print(add(2, 3, 4))
