print("hello world")
name= "amit"
age = 20
price = 35.6

age2 = age
print("my name is :",name )
print("my age is :",age2)
print(age)
print("my price is ;", price)

#1
print("hello world")

# variables
name= "amit"
age = 20
price = 35.6

age2 = age
print("my name is :",name )
print("my age is :",age2)
print(age)
print("my price is ;", price)

#2
str = "amit shaw"

print(str[0])
print(str[2])

print(str[0:5])

print (str[:8])
print (str[2:])
print (len(str[:9]))

print(str[-1]) #only in python 
print (str[-3:-7])


str = "i am studying python"
print(str.endswith("python"))
print(str.startswith('i am'))

print (str.find ('studyind'))
print(str.replace('i', 'o'))
print(str.count('o'))


#Shawamit@#₹1

#3
#list

marks = [90,80,65.85,37,57]
print(marks)
print(type(marks))
print(marks[0])
print(marks[4])

student = ["karan",65, "delhi", "arjun"]
print(len(student))
print(student[0])
print(student[1:4]) #slicing 

print(student[0])
student[0] = "amit"
print(student)

list = [1,3,8]
list.append(2) #add at the end 
print(list)
list.sort() #ascending order 
print(list)
list.sort(reverse=True) #descending order
print(list)
list.reverse() #reverse the list
print(list)
 #list.insert(index, element)# insert element at index 
list.insert(1, 4)
print(list)

list.remove(4)
print(list)


 #TUPLES
 #tuples are immutable
tup = (56,75,44,76,54,)
print(tup)
print(type (tup))
print(tup[1:4])

print(tup.count(2))
#index
tup.index(2) #return index of first occurrence


#4
#dictonary            key:value

dict = {"name" :"amit",
        "age"  : 20,
       "cgpa" : 9.8,}
print(dict)
print(dict["name"])

#no index in dictonary

null_dict = {}

student = {
    "name" : "amit",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "maths" : 96,

    }
}

print(student["subjects"]["chem"])
print(len(student))

#methods in dictonary

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

new_dict = {"name" : "anmol" , "age" : 20}
student.update(new_dict)

print(student)

#sets

num = {1,2,4,67,5,4 ,55 }
print(num)
print(type(num))

coll = set()
print(type(coll))

#methods in sets 

coll = { 1,2,5,6,8,33,664,6}

print(coll.pop())
print(coll.pop())

set1 = {1,3,6,5}
set2 = (2,4,6,8,0)

print(set1.union(set2))
print(set1.intersection(set2))

print(set1.difference(set2))

dictionary = {
    "cat": "a small animal",
    "table": ["a piece of furniture","list of facts & figures"]
}

print(dictionary)

subjects = {"python", "java", "c++", "javascript", "python", "java", "c++"}

print(subjects)
print(len(subjects))

marks = {}

x = input("enter phy :")
marks.update({"phy": x})

x = input("enter chem :")
marks.update({"chem": x})

x = input("enter maths :")
marks.update({"maths": x})

print(marks)



#5
#functions 

def sum(x,y):
    s = x+y
    print(s)
    return s
sum(3,5)

def calc_area(radius,pi = 3.14):
    area = pi*radius**2
    print(area)
    return area

calc_area(4)
calc_area(6)

def print_hello():
    print("hello")

print_hello()
print_hello()

print("amit",end=" ")        #built-in function
print("shaw")            

def calc_prod(a,b=5):
    prod=a*b
    print(prod)
    return prod

calc_prod(3,8)
calc_prod(4)

cities =["delhi","mumbai","chennai","kolkata"]
heros =["spiderman", "batman","superman","ironman"]

print(heros[0], end=" ")
print(heros[3], end=" ")
print(cities[1])

def print_len(list):
    print(len(list))
    return len(list)

print_len(cities)
print_len(heros)

def print_fact(n):
    fact= 1
    for i in range(1,n+1):
        fact= fact*i
    print(fact)
    return fact

print_fact(6)
print_fact(32)

def con(usd):
    inr = usd * 86.5
    print(usd,"USD =",inr, "INR")
    return inr

con(7)
con(54)
con(100)

#recursion



#6
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


#7
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

#multiple inheritance

class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()      

print(c1.varC)
print(c1.varB)
print(c1.varA)

#super method:

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print ("car started.")

        @staticmethod
        def stop():
            print("car stopped.")

class ToyotaCar(Car):
    def __init__(self,name, type):
        super().__init__(type)
        self.name = name
        super().start()
        
car1 = ToyotaCar("prius", "electric")
print(car1.type)


class person:
    name = "anonymous"

   # def changeName(obj, name):
   # self.__class__.nmae = "rahul" 

    @classmethod
    def changename(cls, name):
        cls.name = name

                                           #1.static method
                                           #2.class method  (cls)
                                           #3. instance method (self)
p1 = person()
p1.changename("rahul")
print(p1.name)
print(person.name)


# property method

class student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"


stu1 = student(95,80,92)
print(stu1.percentage)

stu1.chem = 100
print(stu1.percentage)

#polymorphism