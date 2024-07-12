class Person:
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def describe(self):
        print(f"my name is {self.name} i am {self.age} I am {self.height}inches tall")
class Student(Person):
    def __init__(self, name, age, height,dept,hobby):
        self.dept=dept
        self.hobby=hobby
        super().__init__(name, age, height)
        
        print(f" My name is {self.name}, I am {self.age}yr,I am in the {self.dept}, I love to {self.hobby}")

class lecturer(Person):
    def __init__(self, name, age, height,rank,specilization):
        self.rank=rank
        self.spec=specilization
        super().__init__(name, age, height)
        print(f"MY name is {self.name}, I am {self.age},I am a {self.rank}, My area of specilization is {self.spec}")
    def school(self,sname):
        print(f"my name is {self.name},I am {self.age}yrs, I am an {self.rank},I lecture at the {sname} My area of specilization is{self.spec}")
l1=lecturer('Doctor Ajijolakeu',50,145,"Ass.Professor",'Industrial Microbiology')
l1.school('university of ilorin ')
S1=Student('musa bashirat', 24,125,'chemistry','football')
              
class BankAccount:
    def __init__(self,account_number, account_name, account_balance):
        self.account=account_number
        self.name=account_name
        self.balance=account_balance
    def GTB (self):
              print(f'my name is {self.name},My account number is {self.account},my balance is {self.balance}, Thanks for banking with us')
    def deposit(self,amount):
         self.balance+=amount
         print(f'dear {self.name}, you made a deposit of {amount} and your account balance is {self.balance}')

    def withdrawal(self,amount):
        if self.balance<amount:
               print('Your account is insufficient,kindly deposit more amount to enjoy our service!')
               return
        self.balance-=amount
        
        print(f'dear {self.name},you just made a withdrawal of {amount}, your main balance is {self.balance}')

    def check_balance(self):
        print(f'dear {self.name},Your acccount balance is {self.balance},Thanks for banking with us')
c1=BankAccount(11111, "BASHIRAT MUSA", 1000000,)
c1.deposit(5000)
c2=BankAccount(455577,'OMOTARA Aminat',5000)
c2.withdrawal(45000)
c3=BankAccount(11111111,'OMOTARA sunkanmi','$50000')
c3.check_balance()


