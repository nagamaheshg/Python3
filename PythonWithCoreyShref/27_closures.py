# Closures

# A Closure is an inner function that remember and access to variable in the local scope which it was created even after the outer function finish it of it's execution 

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)


def outer_func(msg):
    message = msg
    
    def inner_func():
        print(message)
        
    return inner_func

hi_func = outer_func('hi')
hello_func = outer_func('hello')
hi_func()
hello_func()

def logger(func):
    
    def log_func(*args):
        logging.info(f'Running "{func.__name__}" with arguments {args}')
        print(func(*args))
        
    return log_func

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

add_logger = logger(add)
sub_logger = logger(sub)
add_logger('10', 20)
sub_logger(20, 10)