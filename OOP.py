class MyClass:
    pass  
obj = MyClass()

# Instance Variables

class MyClass:

    def increment(self):
        if not hasattr(self, 'instance_var'):
            self.instance_var = 0
            self.instance_var += 1
            return self.instance_var 
        obj = MyClass() 
        print(obj.increment())  
print(obj.increment())


#Class Variables

class MyClass:
    class_var = 0  

    def increment(self):  
        MyClass.class_var += 1  

obj1 = MyClass()  
obj2 = MyClass()  

print(MyClass.class_var)  
obj1.increment()  
print(MyClass.class_var)  
obj2.increment()  
print(MyClass.class_var)  


# Methods in class

class MyClass:
    def my_method(self):  
        print("This is a normal method.")  
obj = MyClass() 
obj.my_method()  

#  class method

class MyClass:
    class_var = 0  

    def increment(self):  
        MyClass.class_var += 1  

obj1 = MyClass()  
obj2 = MyClass()  
print(MyClass.class_var)  
obj1.increment()  
print(MyClass.class_var)  
obj2.increment()  
print(MyClass.class_var)  