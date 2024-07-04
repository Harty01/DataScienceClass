class Person:
    def __init__ (self,fname,lname,age,sex,):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.sex=sex
    def describe(self):#method
        print(self.fname, self.lname, self.age, self.sex)

p1=Person("musa","bashirat",3,"F")
p1.describe()
# print(p1.fname)

# class Student(Person):
#     def __init__(self,fname,lname,age,sex,cname):
#      self.cname=cname
#      super().__init__(fname,lname,age,sex)
#     def describe(self): 
#         print(f"my name is {self.fname} {self.lname} i am {self.age}yrs, i am in basic {self.cname}")

# x=Student("tola","dayo",24,"F",2)
# x.describe() 
# class Lecturer(Person):
#     def __init__(self, fname, lname, age, sex,dept):
#         self.dept="microbiology"
#         super().__init__(fname, lname, age,sex)
#         print(f"my name is {fname},{lname},i am {age}yrs old,,I'm a{self.sex} I am in the{dept} department")
# t1=Lecturer("bola","kemi",37, "female","chemistry")
# t1.describe()
# class Student(Person):
#     def new_student(self,level): #another method without using the init method
#         self.level=level
#         print(f"my name is {self.fname} {self.lname} {self.age} {self.sex} {self.level} level")
# c1=Student("bola","segun",24,"F")
# c1.new_student(500)


        
    
class Gtbank():
    def __init__(self,acctname,acctnumber,acctbalance=0) :
        self.acctname=acctname
        self.acctnumber=acctnumber
        self.acctbalance=acctbalance
    def ask(self):
        print(f"i am {self.acctname} my acct number is {self.acctnumber} my balance is {self.acctbalance} i love gtbank")

# # c1=Gtbank("musa bashirat",130142474,12000) 
# c1.ask()
# class Deposit(Gtbank):
#     def __init__(self, acctname, acctnumber, acctbalance):
#         super().__init__(acctname, acctnumber, acctbalance)
#     # def deposit(self,amount):
#     #     if amount > 0:
#     #         self.acctbalance+=amount
#     #         print(f"you are wonderful {self.acctbalance}")
# c1=Deposit("musa bashirat",130142474,12000)
# c1.deposit(3000)
    def new_balance(self,amount):
        self.acctbalance-=amount
        print(f"you just make a withdrawal of {amount} your acct balance is {self.acctbalance}")
c1=Gtbank("musa bashirat",130142474,12000)
c2=Gtbank("adijat",1111111,80000)
c1.new_balance(3000)
c2.new_balance(7000)
# class withdrawal(Gtbank):
#     def __init__(self, acctname, acctnumber, acctbalance):
#         super().__init__(acctname, acctnumber, acctbalance)
#     def withdrawal(self,amount):
#         if self.acctbalance<amount:
#             print('INSUFFICIENT FUND')
#             return
#         self.acctbalance-=amount
#         print(f"you just made a withrawal of {amount} and your acct balance is {self.acctbalance}")
# a1=withdrawal("dammy",777777,8000)
# a1.withdrawal(7000)


    



            

