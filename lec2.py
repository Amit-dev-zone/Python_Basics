# Condotional statements -  if(t/f) , else, elif()

age = 21

if age >= 18:
    print("you can vote")
    print("you can't vote")

color = input("enter color: ")

if color == "red":
    print("stop")
elif color == "green":
    print("go")
if color == "yellow":
    print("look")
else: 
    print("wrong color for traffic input")



age = int(input("enter age: "))

if (age < 13):
    print("child")
elif (age >= 13 and < 18):
    print("teen")
if (age >= 18):
    print("adult")
else: 
    print("wrong age for input")


username = input("enter username: ")
password = input("enter password: ")

if(username == "admin" and password == "pass"):
   print("login successful")
elif(username != "admin"):
   print("wrong username")
else:
   print("Wrong password")


n = input("enter number: ")

if(n%2 == 0):
    print("even number")
else:
   print("odd number")

# Nesting

username = input("enter username: ")
password = input("enter password: ")

if(username == "admin" and password == "pass"):
   print("login successful")
else:
    if(username != "admin"):
       print("wrong username")
    else:
       print("Wrong password")





             # Match Case 

color = input("enter color: ")

match color:
   case "red":
      print("stop")
   case "green":
      print("go")
   case "yellow":
      print("look")
   case _:
      print("wrong color")


     
     # Loops 

# infinite loop 

while True:
    print("helloworld")

count = 1

while (count <= 5):  # terminating condn
    print("hello", count)
    count += 1

i = 1

while(i <= 10):
    print(i)
    i += 1
 

i = 10 # reverse

while(i >= 1):
    print(i)
    i -= 1

  #table 
n = int(input("enter number: "))
i = 1
while(i <= 10):
    print(n*i)
    i += 1


# break and continue 
i = 1

while(i <= 10):
    if(1 % 6 == 0):
        break
    print(i)
    i += 1

print("outside loop now.... ")

i = 0

while(i < 10)
    i += 1
    if(i % 2 == 0):
        continue
    print(i)


# for in loop 

string = "hello"

for var in string:  # in => membership operator
    print(var)

for 'o' in string:
    print("o exist in string")

# range(n) -> 0 to n-1   
  
word = "artificial_intelligence"  # count no of i's
count = 0

for ch in words:
    if(ch == "i"):
        count += 1

print("count of i = ", count)


word = "artificial
count = 0

for ch in words:
    if(ch == "a" or ch == "e" or ch == "i" or ch == "o"or ch == "u"):
        count += 1

print("ans = ", count)

# range(strt, "stop", step)

for i in range(2, 11, 2)



# Function

def hello():
    print("hello")
    print("from python")

hello()
hello()

def sum(a, b):
    s = a + b
    return s

print(sum(3, 4))

def avg(a, b, c):
    s = a + b + c
    return (s/3)

print(avg(3, 4, 7))

def sum(a, b=1):
    return a + b


print(sum(6))

# type - 1.built-in   2. user-defined

# lambda fxn

sum = lambda a, b, c: a+b+c
print(sum(6, 9))


factorial of n 

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
    fact *= i
    return fact
    
n = int(input("enter n: "))
print(cal_fact(n))


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

print("amit",end=" ")        
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













