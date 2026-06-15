#OBJECT ORIENTED PROGRAMMING SYSTEM

#redundency dec     reusability inc
#class - blueprint of an object !   -----> object - instance of class

class car:
    color = "blue"
    brand = "mercedes"

car1 = car()
print(car1.color)
print(car1.brand)

#   __init__function(method)

class Student:
    collage_name = "ABC collage"  # common for object

    def __init__(self, fullname, marks):
      self.name = fullname   # instance
      self.marks = marks
      print("adding new student in database.")
   

s1 = Student("karan",87)
print(s1.name, s1.marks)
print(Student.collage_name)
print(s1.collage_name)


s2 = Student("arjun",96)
print(s2.name, s2.marks)
print(s2.collage_name)


class Students:
   def __init__(self):  #default
      print("object is being constructed..")
   
   def __init__(self, name, cgpa): #parameterized
      self.name = name
      self.cgpa = cgpa

   def get_cgpa(self): #instance attribute 
       return self.cgpa
   
stu1 = Students("Bob", 9.0)
stu2 = Students("Alice", 8.4)
stu3 = Students("Charlie", 9.2)

print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")

print(stu1.cgpa)
print(stu2.name)
print(stu3.name)



#attribute       class and instance attribute

# practice

class Student:
   def __init__(self, name, marks):
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

   # def welcome(self):
   #    print("welcome to the class", self.name)

   # def get_marks(self):
   #    return self.marks


# s1 = Student("karan",96)
# s1.welcome()
# print(s1.get_marks())

#METHODS - instance, class, static

class Laptop:
   storage_type = "ssd"

   def __init__(self, RAM, storage):
      self.RAM = RAM
      self.storage = storage

   @classmethod #decorators
   def get_storage_type(cls): # class method - can access class attribute only
      print(f"storage type = {cls.storage_type}")

   def get_info(self):  # instance method - can access class and instance attribute 
      print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

   @staticmethod
   def calc_discount(price, discount):
      final_price = price - (discount * price / 100)
      print(f"discounted price = {final_price}")

l1 = Laptop("16gb", "512gb")
l2 = Laptop("8gb", "256gb")

l1.get_info()
Laptop.get_storage_type()
l1.get_storage_type()
l1.calc_price(40_000, 10)


#  # question   create a class of bank account with 2 attributes-- balance and acc no. create  methods for debit,credit & printing .

# class Account:
#    def __init__(self,bal,acc):
#       self.balance = bal
#       self.acc_no = acc

# #debit method
# def debit(self, amount):
#    self.balance -= amount
#    print("Rs.",amount,"was debited")

# def credit(self,amount):
#    self.balance += amount
#    print("Rs",amount,"was credited")

# def get_balance(self):
#    return self.balance     


# acc1 = Account(1000,12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)


class Product:
   count = 0

   def __init__(self, name, price):
      self.name = name
      self.product = product
      Product.count += 1

   def get_info(self): #instance method
       print(f"price of {self.name} is Rs.{self.price}")

   @classmethod
   def get_count(cls):
      print(f"total product in store = {cls.count}")
   
   @staticmethod
   def calc_discount(price, discount):
      print(f"discounted price = {price -(discount * price / 100)}")

p1 = Product("phone", 10_000)
p2 = Product("laptop", 50_000)
p3 = Product("pen", 10)

p1.calc_discount(p1.price, 12)

#Data hiding
# public, protected, private

class BankAccount:
   def __init__(self, name, balance):
      self.name = name #public
      self._balance = balance #protected
      self.__balance = balance #private - data mangling

   def get_balance(self): #getter
       return self.balance

   def set_balance(self, newBalance): #setter
       self.__balance + newBalance
       
acc1 = BankAccount("Alice", 100_000)
acc1.set_balance(200_000)

print(acc1.name. acc1.get_balance())
print(acc1.name. acc1._BankAccount__balance)


# Inheritance 

#single inheritance                           #multi level inheritance
class Car:
    @staticmethod
    def start():
        print ("car started.")

        @staticmethod
        def stop():
            print("car stopped.")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("diesel") 
car1.start()       



class Employee:
    start_time = "10am"
    end_time = "6pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

t1 = Teache("Math")
t1.change_time("5pm")
print(t1.subject, t1.start_time, t1.end_time)


staff1 = AdminStaff("Manager")
print(staff1.subject, staff1.start_time, staff1.end_time)



#multiple inheritance

class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
       super.__init__(salary)
       Student.__init__(self, gpa)
       self.name = name

ta1 = TA(15_000, 9.3, "shradha")
print(ta1.name, ta1.ta1.gpa, ta1.salary)



#Encapsulation           
#Encapsulation is the bundling of data and methods that operate on that data within one unit, or class.

# Abstraction
# Abstraction is hiding the impletation details and showing only the essential features of the object.


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cow(Animal):
    def make_sound(self):
        print("Moo")

lion = Lion()
lion.make_sound

cow = Cow()
cow.make_sound




#polymorphism - many forms

print(1+2, "hello"+"world")

class Employee:
    def get_designation(self):
        print("designation = Employee")

class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")

t1 = Teacher()
t1.get_designation()
        


class Teacher():
    def get_designation(self):
        print("designation = Teacher")

class Accountant():
    def get_designation(self):
        print("designation = Accountant")

t1 = Teacher()
t1.get_designation()
        
acc1 = Teacher()
acc1.get_designation()
        