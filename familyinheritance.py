class Parent:
    def __init__ (self,fname,lname,age,job):
        self.fname=fname
        self.lname=lname
        self.age=age
        self.job=job
    def describe(self):
        print(f"my name is {self.fname}{self.lname}, i am {self.age} yrs old,i am an {self.job}")
    def first_gen(self,work):
        print(f"I am {self.job},i work in {work}")
c1=Parent("musa","bashirat","engineer",24)
# c1.describe()
# c1.first_gen("cheveron")
class Child(Parent):
    def __init__(self,fname,lname,age,job,school,grade):
        super().__init__(fname, lname, age, job)
        self.school=school
        self.grade=grade
    # def child1(self):
        # print(f"my name is {self.fname},I am {self.age}yrs old,I attends {self.school},I am a {self.grade}student")  
    def child2(self,rname,study):
        print(f"my name is {self.fname} {rname},I am {self.age} yrs old,I attend {self.school} I study {study},I am a {self.grade} student")     

s1=Child("musa","bashiart",24,"age","uniloin","first class")
s1.child2("bashirat","microbiology")
class Grandchild(Child):
    def __init__(self, fname, lname, age, job, school, grade,rname,favorite_toy,favorite_game):
        super().__init__(fname, lname, age, job, school, grade)
        self.toy=favorite_toy
        self.game=favorite_game
        self.realname=rname
    def play(self):
        print(f"my name is {self.fname} {self.realname},I atttend {self.school},My favorite game is {self.game},I love to play with {self.toy}")
g1=Grandchild("badmus","Abdulrofiu",34,"storekeeper","unilorin","secondclass","samsu","building blocks","football")
g1.play()
#     def classs(self,basic):
#         print(f"my name is {self.lname},{self.realname},my family name is {self.fname},I am in primary {basic}")
# gig1=Grandchild("badmus","Abdulrofiu",34,"storekeeper","unilorin","secondclass","samsu","building blocks","football")
# gig1.classs("four")