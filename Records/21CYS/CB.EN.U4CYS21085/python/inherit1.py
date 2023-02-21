class Parent():
    def __init__(self):
        self.value = "Inside Parent"
    def show(self):
        print(self.value)
        
class Parent2():
    def display(self):
        print("Inside Parent2")

class Child(Parent, Parent2):
    def __init__(self):
        self.value = "Inside Child"
    def show(self):
        print(self.value)

obj1 = Parent()
obj2 = Child()
obj1.show()
obj2.show()
obj2.display()