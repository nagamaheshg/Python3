# Dunder methods or special magic methods

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first+self.last+'@gmail.com'
        
    def fullname(self):
        
        return self.first+' '+self.last
    
    def apply_raise(self):
        
        self.pay = self.pay * self.raise_amount
        return self.pay
    # by using repr unambiguous representation of object should used for debugging logging like that
    def __repr__(self):
        
        return f"Employee('{self.first}', '{self.last}', '{self.pay}'')"

    # str is more readable representation of object met to be used display to end user.
    def __str__(self):
        
        return f'{self.fullname()} - {self.email}'
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname)
    
print('test'.__len__())
    
    
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)
print(emp_1)

print(emp_1+emp_2)
print(len(emp_1))

# print(repr(emp_1))
# print(str(emp_1))

# (or)
print(emp_1.__repr__())
print(emp_1.__str__())

print(1+2)
print(int.__add__(1,2))
print(str.__add__('1','2'))
