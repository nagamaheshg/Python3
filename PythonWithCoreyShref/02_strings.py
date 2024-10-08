# string represent in single quote or double quote
message = 'Hello World'    # message is variable.
print(message)             # print is one built-in function in python

# len() is another built in function in python
print(len(message))

# index start from zero 
print(message[0])   # To accessing first character in the string 

# slicing to get substring of string
""" 
    syntax string[start: stop(exclude): step_size(optional)]
    
    if we not specify the start value it's start taking from beginning
    if we not specify the end value it's start taking from end of the string
    Step size is optional value no of characters need jump
    
"""
print(message[0:6]) 
"""String Methods
    upper()-convert to uppercase letters
    lower()-convert to lowercase letters
    count()-takes an argument
    find() - takes an argument if it find provide start index. or else return -1
    replace('old', 'New') - return the value won't modify existing string
    dir('message') - it takes one argument it returns all method available under that data type
    help('datatype')
    """
print(message.upper()) 
 
greeting = 'Hello'
name = "Mahesh"

print(greeting+", "+name+' '+'Welcome') # concat strings by using + another way  is format f'string format method'

print(f'{greeting}, {name} Welcome')
 
