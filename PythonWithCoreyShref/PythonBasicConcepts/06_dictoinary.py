# Dictionaries - Working with key-value pairs
# Key is unique identifier - value that data

student = {
    'name': 'john',
    'age': 25,
    'courses': ['Math', 'CompSci']
}
print(student)

print(student['name'])
print(student['courses']) 

# in dictionaries keys actually any immutable datatype

#student['phone'] #getting KeyError

# if suppose key doesn't exist in that time return none 

print(student.get('phone'))

# if key doesn't exist return default value.
print(student.get('phone', 'Not found'))

student['phone'] = '+91 9052-932-167'
print(student.get('phone', 'Not found')) # if key found print the key value or else ignore

# we can also update existing value by using update method. by using update we can update multiple values

student.update({'name':'jane','age':23, 'phone': '+91 9848022338'})
print(student)

# del to delete an existing data we are using del
del student['age']
print(student)
# we can also use pop method to delete the key:value pair and also. pop also remember what value it deleted.

popped_data = student.pop('name')
print(popped_data)

student.update({'name':'jane','age':23, 'phone': '+91 9848022338'})
print(student)

print(len(student))
# .keys() method return all keys in dictionary
keys = student.keys()
keys = list(keys)
print(keys)

# .values() method return all values in dictionary
values = student.values()
values = list(values)
print(values)

for key in keys:
    print(f'{key}: {student[key]}')
    
# .items() method returns all key:value items as tuples
for key, value in student.items():
    print(f'{key}: {value}')

students = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 75,
    'Diana': 95,
    'Eve': 88
}

threshold = 90
passed_students = {name: grade for name, grade in students.items() if grade > threshold}
print(passed_students)