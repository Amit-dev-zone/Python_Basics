#OBJECT ORIENTED PROGRAMMING SYSTEM

#redundency dec     reusability inc
#class -----> object

class car:
    color = "blue"
    brand = "mercedes"

car1 = car()
print(car1.color)
print(car1.brand)

#   __init__function

class Student:
    collage_name = "ABC collage"    #common object

    def __init__(self, fullname, marks):
      self.name = fullname
      self.marks = marks
      print("adding new student in database.")

s1 = Student("karan",87)
print(s1.name, s1.marks)

s2 = Student("arjun",96)
print(s2.name, s2.marks)
print(s2.collage_name)



#attribute       class and instance attribute

#METHODS

def welcome(self):
   print("welcome to the class", self.name)

def get_marks(self):
   return self.marks


s1 = student("karan",96)
s1.welcome()
print(s1.get_marks())

# practice

class Student:
   def __init__(self,name,marks):
    self.name = name
    self.marks = marks
    
def get_avg(self):
    sum = 0
    for val in marks:
       sm += val
    print("hi",self.name,"your avg score is:",sum/3)
    
s1 = Student("tony stark",[99,95,89])

s1.name = "ironman"
s1.get_avg()


# static method   work at class level

class Student:
   @ststicmethod
   def collage():
      print("ABC Collage")


            
 # abstraction     # Encapsulation           
 # Abstraction is hiding the impletation details and showing only the essential features of the object.
 # Encapsulation is the bundling of data and methods that operate on that data within one unit, or class.

 # question   create a class of bank account with 2 attributes-- balance and acc no. create  methods for debit,credit & printing .

class Account:
   def __init__(self,bal,acc):
      self.balance = bal
      self.acc_no = acc

#debit method
def debit(self, amount):
   self.balance -= amount
   print("Rs.",amount,"was debited")

def credit(self,amount):
   self.balance += amount
   print("Rs",amount,"was credited")

def get_balance(self):
   return self.balance     


acc1 = Account(1000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
