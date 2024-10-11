
from functools import wraps

def my_logger(original_fun):
    import logging
    logging.basicConfig(filename=f'{original_fun.__name__}',level=logging.INFO)
    @wraps(original_fun)
    def wrapper(*args, **kwargs):
        logging.info(f'Ran with args:{args} and kwargs: {kwargs}')
        return original_fun(*args, **kwargs)
    
    return wrapper

def outer_function(msg):
    
    message = msg
    
    def inner_function():
        print(message)
    
    return inner_function

hi_func = outer_function('Hi')
bye_func = outer_function('Bye')
hi_func()  # remember the message variable. even outer function is executed
bye_func()  # remember the message variable. even outer function is executed

# decorators

'''
    A decorator is just  function that take another function as an argument some kind of functionality and return another function
    all of these without altering the source code of original function that you passed in.
'''

def decorator_function(original_fun):
    
    def wrapper_function():
        print(f'Wrapper executed before {original_fun.__name__}')
        return original_fun()
    
    return wrapper_function

@decorator_function
def display():
    print('Display function ran')
display()

# or
display = decorator_function(display)
display()


''' decorating our function allow us easily add the functionality to existing functions by adding that functionality inside the wrapper. for example in the above display function without modifying inside wrapper i can add any kind of code here'''
def my_decorator_func(original_func):
    
    @wraps(original_func)
    def wrapper_func(*args, **kwargs):
        print(f'Wrapper executed before {original_func.__name__}')
        original_func(*args, **kwargs)
    
    return wrapper_func

@my_decorator_func
def display_info(name, age):
    print(f'Display Info ran with arguments {name} {age}')

display_info('Naga Mahesh Gatta', 31)

class decorator_class(object):
    
    def __init__(self, original_func):
        self.original_func = original_func
        
    
    def __call__(self,*args, **kwargs):
        print(f"call method executed this before {self.original_func.__name__}")
        return self.original_func(*args, **kwargs)
    
@decorator_class
def display():
    print('display function is ran')
    
display()



import time

def my_timer(original_func):
    
    @wraps(original_func)
    def wrapper(*args, **kwargs):
        
        t1 = time.time()
        result = original_func(*args, **kwargs)
        t2 = time.time() -t1
        print(f'{original_func.__name__} ran in {t2} sec')
        return result
    
    return wrapper

@my_timer
@my_logger
def add(x, y):
    return x+y

print(add(10, 20))
        
@my_timer
def sub(x, y):
    time.sleep(1)
    return x-y

print(sub(30, 20))

@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print(f'display info ran with arguments{name}{age}')

display_info('Naga Mahesh Gatta', 31)