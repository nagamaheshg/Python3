
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
        self.email = self.first_name+self.last_name+'@gmail.com'
        self.pay = pay
        
        Employee.number_of_employees += 1
    
    def display_full_name(self):
        print(f'{self.first_name} {self.last_name}')
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        print(self.pay)
        
emp_1 = Employee(first_name='Naga Mahesh', last_name='Gatta', pay=50000)
emp_2 = Employee(first_name='Test', last_name='User', pay=60000)

emp_1.display_full_name()
emp_2.display_full_name()

#Employee.raise_amount = 1.05 # It reflected all of instances and Employee
emp_1.raise_amount = 1.05 #

emp_1.pay
print(emp_1.raise_amount)
print(emp_1.__dict__)
print(Employee.__dict__)
emp_1.apply_raise()

emp_2.pay
print(emp_2.raise_amount)
emp_2.apply_raise()

print(f'Total Number of Employees: {Employee.number_of_employees}')