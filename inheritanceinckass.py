class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def describe(self):
        print(f"my name is {self.name} i am {self.age} I am {self.height}inches tall")
class Student(Person):
    def __init__(self, name, age, height,dept):
        self.dept=dept
        super().__init__(name, age, height)
        self.dept=dept
    
        print(f"the name is {self.name} I am {self.age} years old)
              
              +
              
              
              
              
              
              
              ")

