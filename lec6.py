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

