# sorting list, tuples and objects

li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li, reverse=True)
print(f'sorted variable:\t', s_li)
print(f'original Variable:\t', li)

# There is one difference between sorted function and sort method. sorted function return a new sorted list.
li.sort()
print(f'sorted variable:\t', s_li)
print(f'original Variable:\t', li)


tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print('Tuple\t: ',s_tup)

di = {'name': 'corey', 'job':'Programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t', s_di)

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li)

class Employee():
    
    def __init__(self, name, age, salary):
        self.name = name,
        self.age = age,
        self.salary = salary

    def __repr__(self):
        return (f"{self.name}{self.age}{self.salary}")
    

e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]

# custom function to sort
def e_sort(emp):
    return emp.name 

s_employees = sorted(employees, key=e_sort, reverse=True)
s_employees = sorted(employees, key=lambda e: e.name, reverse=True)


print(s_employees)