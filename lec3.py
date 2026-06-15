str = "amit shaw"    # string - immutable
str2 = "python"
sentence = str + " " + str2


print(len(str))
print(len(str2))
print(sentence)

for ch in sentence:
    print(ch, end=" ")

print(str[0])
print(str[2])

#substrings
print(str[0:5]) # 0 to 4

word = "ApnaCollege"
print(word[0:10]) # slicing

print (str[:8])
print (word[2:])
print (len(str[:9]))

print(str[-1]) #only in python 
print (str[-3:-7])


str = "i am studying python"
print(str.endswith("python"))
print(str.startswith('i am'))

print (str.find ('studying'))
print(str.replace('i', 'o'))
print(str.count('o'))


# string formatting - .format , f-string
a = 5
b = 10
sum = a + b

#normal formatting
print("language is {}".format("python"))
print("sum of {} & {} is {}".format(a, b, sum))

#index based formatting
print("sum of {0} & {1} is {2}".format(a, b, sum))

#value based formatting
print("value of vars {a} & {b}".format(a=4, b=7))

# f-string
a = 5
b = 10

print(f"sum of {a} & {b} is {a + b}")
print(f"avg of {a} & {b} is {(a + b)/2}")


                #   >>>>>>  #List - mutable >>>>>>

marks = [90,80,65.85,37,57]
print(marks)
print(type(marks))
print(marks[0])
print(marks[4])
print(marks[-5:-2]) # 80, 65, 85

student = ["karan",65, "delhi", "arjun"]
print(len(student))
print(student[0]) 
print(student[1:4]) #slicing 

print(student[0])
student[0] = "amit"
print(student)
              


            #    >>>>> list methods >>>>>>
list = [1, 3, 8, 6, 14]
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

x = 6
idx = 0

for val in list:
    if(val == x):
        print(f"{x} is found at idx = {idx}")
        break
        idx += 1



#TUPLES - tuples are immutable
 
tup = (56, 75 ,44 ,76 ,54 ,"abc", "3.14")
tuple = (1,)
print(tup)
print(type (tup))
print(tup[1:4])

print(tup.count(2))

sum = 0
for val in tup:
    sum += val

print(f"sum of vals is {sum}")


                      # methods
tup.index(2) #return index of first occurrence
tup.count()

print(tup[:])



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
print(list(dict.get(age)))

new_dict = {"name" : "anmol" , "age" : 20}
student.update(new_dict)   #mutable and unordered

print(student)

                 #SETS

num = {1, 2, 4, 67, 5, 55, 4, 2}
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

set1.add(4)
set1.remove(6)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
set1.remove() #empties the set 


dictionary = {
    "cat": "a small animal",
    "table": ["a piece of furniture","list of facts & figures"]
}

print(dictionary)

subjects = {"python", "java", "c++", "javascript", "python", "java", "c++"}

print(subjects)
print(len(subjects))

marks = {} # dictonary 

x = input("enter phy :")
marks.update({"phy": x})

x = input("enter chem :")
marks.update({"chem": x})

x = input("enter maths :")
marks.update({"maths": x})

print(marks)


# problem - unique courses

info = {
    ["Alice", "English"],
    ["Bob", "Science"],
    ["Alice", "Math"],
    ["Alice", "Science"],
    ["charlie", "Math"],
    ["Alice", "Physics"],
    ["Bob", "English"],
    ["Alice", "Math"],
}
#1
courses_set = set()

for tup in info:
    courses_set.add(tup[1]) 

print(courses_set)

for name, course in info:
    print(name, course)

#2
for name, course in info:
    if(courses == "English")
    print(nums)

#3
 dictn = {}

for name, course in info:
    if dictn.get(name) == None:    #name dont exist in dictonary   
    dictn.update({name: set()}) 
    dictn[name].add(course)
    else:
    dictn[name].add(course)   

print(dictn)