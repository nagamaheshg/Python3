# python Object-Oriented Programming

# classes associate "attributes" and "functions" or "methods"
# classs is a blueprint to create unique employee

class Employee:
    
    def __init__(self,first_name, last_name, pay):
        
        # attributes
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name+self.last_name+'@gmail.com'
        self.pay = pay
    
    def display_full_name(self):
        print(f'{self.first_name} {self.last_name}')
        
emp_1 = Employee(first_name='Naga Mahesh', last_name='Gatta', pay=50000)
emp_2 = Employee(first_name='Test', last_name='User', pay=60000)

emp_1.display_full_name()
emp_2.display_full_name()


# we don't have much benfit of using classes if we did it this way.
# to  make this setup automatically to create an employee we gone use special method init

# emp_1.first_name = 'Naga Mahesh'
# emp_1.last_name = 'Gatta'
# emp_1.email = 'nagamaheshgatta@gmail.com'
# emp_1.pay = 60000

# emp_2.first_name = 'Corey'
# emp_2.last_name = 'Schafer'
# emp_2.email = 'corey.schafer@gmail.com'
# emp_2.pay = 100000

# print(emp_1)
# print(emp_1)
