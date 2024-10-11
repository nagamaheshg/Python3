# how to use property decorator.
# class attributes Getters, Setters, and Deleters

class Employee:
    
    def __init__(self, first, last):
        
        self.first = first
        self.last = last
        # email attribute depends on first name and last name
        # self.email = self.first+self.last+'@gmail.com'
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self):
        
        return f'{self.first} {self.last}'
    
    @fullname.setter
    def fullname(self, name): 
        
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self): 
        print('Delete Name! ')
        self.first = None
        self.last = None 
    
emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim' #

print(emp_1.first)   # first name changed to "JIM". Email printing same 'johnsmith@gmail.com' full name method doesn't have this problem. because every time we run the full name  it get current first name and current last name.

# emp_1.fullname = 'Corey Schafer' # gettering Attribute Error: can't set attribute 

# after setting setter method now this will work
emp_1.fullname = 'Corey Schafer'
 
# By using property decorator allows us to define property method we can access like an attribute
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname