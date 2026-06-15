f = open("file.txt", "w")

data = f.read()
print(data)

data = f.readline()
print(data)
print(len(data))

f.write("text to overwrite \n the complete data.")

with open("file.txt", "r") as f:
    data = f.read()

f = open("sample.txt", "a")

f.write("New text being appended\n to the file")


f = open("sample.txt", "w+")
f.write("123")
print(f.read())

f.close()

   delete file
import os
os.remove("sample.txt")


Activity 

data = True
line = 1
word = "store"

with open("sample.txt", "r") as f:
    while data:
        data = f.readline()

    if(word in data):
        print(f"{word} found at line {line}")
        break

    line += 1

Exception Handling

try:
    x = int(input("enter x: "))
    ans = 10/x

except ZeroDivisionError:
    print("Divided by 0 is not allowed")

except ValueError:
    print("invalid input")

else:
    print(f"ans = {ans}")

finally:
    print("end of program")

   # list comprehension
squares = []

for i in range(6):
    squares.append(i*i)

print(squares)

sq = [i*i for i in range(6)]
print(sq)

nums = [-2, -3, 5, 2, 9, 1]
nums = [0 if val < 0 else val for val in nums]
print(nums)

words = ["hello", "python", "apnacollege"]

print(words[0].upper())

words = [val.upper() for val in words]
print(words)


import json

json_str = '{"name": "Amit","isTeacher": true}'

py_obj = json.loads(json_str)

print(type(json_str))
print(type(py_obj), py_obj)

py_obj = {
    "name": "Shradha",
    "isTeacher": True
}

json_str = json.dumps(py_obj)

print(type(json_str), json_str)

with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(type(py_obj))


data = {
    "name": "Shradha",
    "age": 27,
    "isTeacher": True
}

with open("data.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)

