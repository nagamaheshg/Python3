# Inheritance and subclasses in python

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        
        self.first = first
        self.last = last
        self.email = self.first+self.last+'@gmail.com'
        self.pay = pay
        
    def full_name(self):
        
        return self.first+' '+self.last
    
    def amount_raise(self):
        
        self.pay = int(self.pay * self.raise_amount)
        return self.pay

class Developer(Employee):
    
    raise_amount = 1.10
    def __init__(self, first, last, pay, programming):
        super().__init__(first, last, pay)
        self.programming = programming
    
# we can n't pass mutable data as default arguments like list, dict
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.full_name())
    
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emp()

print(dev_1.pay)
dev_1.amount_raise()
print(dev_1.pay)
print(dev_1.email)
print(dev_1.programming)


# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)

# python have two built-ins functions called

# 1. isinstance() - tell us if an object is instance of a class

print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

# 2. issubclass()

print(issubclass(Manager, Employee))
