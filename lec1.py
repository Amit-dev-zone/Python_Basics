print("hello world")

# variables
name= "amit"
age = 20
_price = 35.6
A = True  # False , None

# age != Age

age2 = age
print(age)
print("my name is :",name )
print("my age is :",age2)
print("my price is :", _price)


print(type(age))
print(type(name))
print(type(A))
print(type(_price))

# keywords - cant be used as a variable name

"'
this is a multi line comment
'"

#operators in python
# arithmatic

a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
# print(a//b)

# relational operators

print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

# assignment operators

a = b
a += 2
b -= 1

print(a)
print(b)


# logical - not, and, or 

# type

ans1 = int(5 + 10.0) #casting
ans2 = 5 + 10.0 #conversion

print(ans1, type(ans1))
print(ans2, type(ans2))

val = bool(10)

print(val, type(val))

#user input - string

#sum of 2 nums

a = int(input("enter a:" ))
b = int(input("enter b:" ))

sum = a + b
print(sum)

