class OverloadDemo:
   def multiply(self,a,b):
       print(a*b)
   def multiply(self,a,b,c):
       print(a*b*c)
m=OverloadDemo()
m.multiply(5,10)

'''
op-
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-6-623185909d04> in <module>
      5        print(a*b*c)
      6 m=OverloadDemo()
----> 7 m.multiply(5,10)

TypeError: multiply() missing 1 required positional argument: 'c'

'''
'''
However, Python does not allow method overloading based on type, number or sequence of method parameters. 
In Python, method overloading is a technique to define a method in such a way 
that there are more than one way to call it. This is different from other programming languages.
'''
class methodOverloading :
    def greeting(self, name=None):
        if name is not None:
            print(“Welcome “ + name)
        else:
            print(“Welcome”)

# Create an object referencing by variable ob
ob = methodOverloading()
# call the method greeting without parameter
ob.greeting()
# call the method with parameter
ob.greeting(‘Donald Trump’)

'''
Output:

Welcome
Welcome Donald Trump
'''
