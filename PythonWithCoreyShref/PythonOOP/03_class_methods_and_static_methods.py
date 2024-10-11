# Difference between regular methods, class methods and static methods

# Regular Methods
'''
    Regular methods in a class automatically takes instance as first argument(self)
    
'''
# class Methods
'''
    To turn regular method to class methods is easy adding decorator to the top (@classmethod)
    
'''
import datetime
import time
class Employee:
    
    # class variables are variables are shared among all instances of class. 
    # instance variable are unique. class variable same for each instance
    # class variable
    raise_amount = 1.04
    number_of_employees = 0
    
    def __init__(self,first_name, last_name, pay):
        
        # attributes # these are attributes for all instances. # instance variable
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name+self.last_name+'gmail.com'
        self.pay = pay
        
        Employee.number_of_employees += 1
    
    def display_full_name(self):
        print(f'{self.first_name} {self.last_name}')
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        print(self.pay)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
        
    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        
    # Additional Constructor
    @classmethod
    def fromtimestamp(cls, t):
        '''Construct a date from a POSIX timestamp (like time.time()). '''
        y, m, d, hh, mm, ss, weekday, jday, dst = time.localtime(t)
        return cls(str(d), str(m), str(y))
    
    @classmethod
    def today(cls):
        '''Construct a date from a POSIX timestamp (like time.time()). '''
        t = time.time()
        return cls.fromtimestamp(t)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        
        return True
            
    
emp_1 = Employee(first_name='Naga Mahesh', last_name='Gatta', pay=50000)
emp_2 = Employee(first_name='Test', last_name='User', pay=60000)

emp_1.display_full_name()
emp_2.display_full_name()
emp_str_1 = 'John-Doe-70000'
emp_3 = Employee.from_string(emp_str_1)

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# instead of doing this 
# first, last, pay = emp_str_1.split('-')
# emp_3 = Employee(first, last, pay)
print(emp_3.email)
print(emp_3.pay)

print(Employee.today())  # Prints today's date as a new Employee instance
print(f"Today's Employee: {emp_3.first_name}/{emp_3.last_name}/{emp_3.pay}")

my_date =datetime.date(2024, 10, 11)
print(Employee.is_workday(my_date))