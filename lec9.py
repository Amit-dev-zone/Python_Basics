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