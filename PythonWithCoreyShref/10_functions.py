# functions created by using def keyword def means definition.

def hello_function():
    pass           # we don't do anything for now 

print(hello_function)


def greet():
    print('Hello Functions!')
    
greet()
greet()

# Dry  # Do not repeat

# return statement - return statement is the last statement of function
def hello_func():
    return "Hello Function"  #instead of printing we return the value

output = hello_func().upper()
print(output)

# passing argument to function

def greetings(name):  # name is required parameter for greetings function. It's not a default parameter
    
    return f'Hello {name}'

print(greetings('Naga Mahesh Gatta'))

def hello_fun(greet, name='you'):
    
    return f'{greet} {name}'

print(hello_fun('Hi', name='naga mahesh gatta'))
      
def student_info(*args, **kwargs):     #args handle arbitrary number of positional arguments
                                       # args store data in tuple format.
    print(args)                        #kwargs handle keyword arguments 
    print(kwargs)
    
    
#student_info('Math', 'Art', name='john', age = 22)
courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

#student_info(courses, info)

# to unpack arguments 
student_info(*courses, **info)

# Number of days per month. First value placeholder for indexing purpose
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """return True for leap year, False for non-leap-year."""
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in month in the year."""
    
    if not 1 <= month <= 12:
        return 'Invalid month'
    
    if month == 2 and is_leap(year):
        return 29
    
    return month_days[month]
    
    
print(days_in_month(2020, 2))