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