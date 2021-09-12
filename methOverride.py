class methodOverride1:                          
    def display(self):
        print("method invoked from base class")

class methodOverride2(methodOverride1):
    def display(self):
        print("method invoked from derived class")

ob=methodOverride2()
ob.display()

'''
op-
method invoked from derived class

In order to access the overridden methods in Python we have to use super().
'''
class methodOverride1:                          
    def display(self):
        print("method invoked from base class")

class methodOverride2(methodOverride1):
    def display(self):
        print("method invoked from derived class")
        super().display()

ob=methodOverride2()
ob.display()

'''
op-
method invoked from derived class
method invoked from base class
'''
