class Component:
  
   # composite class constructor
    def __init__(self):
        print('Component class object created...')
  
    # composite class instance method
    def m1(self):
        print('Component class m1() method executed...')
  
  
class Composite:
  
    # composite class constructor
    def __init__(self):
  
        # creating object of component class
        self.obj1 = Component()
          
        print('Composite class object also created...')
  
     # composite class instance method
    def m2(self):
        
        print('Composite class m2() method executed...')
  
        # calling m1() method of component class
        self.obj1.m1()
  
  
# creating object of composite class
obj2 = Composite()
  
# calling m2() method of composite class
obj2.m2()


'''
Output
Component class object created...
Composite class object also created...
Composite class m2() method executed...
Component class m1() method executed...

Explanation:

In the above example, we created two classes Composite and Component to show the Has-A Relation among them.
In the Component class, we have one constructor and an instance method m1().
Similarly, in Composite class, we have one constructor in which we created an object of Component Class. Whenever we create an object of Composite Class, the object of the Component class is automatically created.
Now in m2() method of Composite class we are calling m1() method of Component Class using instance variable obj1 in which reference of Component Class is stored.
Now, whenever we call m2() method of Composite Class, automatically m1() method of Component Class will be called.
'''
