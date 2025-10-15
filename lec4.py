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

