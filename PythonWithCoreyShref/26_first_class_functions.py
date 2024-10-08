# first class functions

def square(num):
    return num * num

def cube(num):
    return num * num * num

# output = square   # output variable is equal to function.
# print(square)
# print(output(5))

# so far we assign function to variable
# a function accept other function as an arguments or return function as result that function called higher order function.

def my_map(func, arg_list):
    
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1,2,3,4,5])
print(squares)

cubes = my_map(cube, [1,2,3,4,5])
print(cubes)


# return a function from an another function.

def logger(msg):
    
    def log_message():
        print('Log: ',msg)
    
    return log_message

log_hi = logger('Hi')
log_hi()

def html_tag(tag):
    
    def wrap_text(content):
        
        print(f'<{tag}>{content}</{tag}>')
    
    return wrap_text

# remembering the previous state
print_h1 = html_tag('h1')
print_h1('Hello How You doing?')

