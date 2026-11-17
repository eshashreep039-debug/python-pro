student={
    "name":"Esha",
    "dept":"CSE",
    "age": 20,
    "marks": 50
}

student["city"]="bangalore"
student["marks"]=90
student.get("age")
print(student)
for key, value in student.items():
    print(key,":",value)
  
print(student.keys())
print(student.values())