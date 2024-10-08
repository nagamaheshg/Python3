# if condition evaluate True or False 

if True:
    print('Conditional True')
    
else:
    print('Condition Failed')
    
language = 'Python'

if language == 'Python':
    print('Language is Python')

elif language == 'Java':
    print('Language is Java')
    
elif language == 'JavaScript':
    print('Language is JavaScript')
    
else:
    print("It's some other programming language might be")
    
# Comparison Operators
'''
Equal ==
Not Equal !=
Greater than >
Greater than or Equal >=
Less than <
Less than or Equal <=
Object Identity is
'''


# False Values:

    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '',(),[].
    # Any empty mapping. For example, {}.
    
# and
# or
# not

user = 'Admin'
logged_in = False

if not logged_in:
    print('Please login')

elif user == 'Admin' and logged_in:
    print('This is Admin Page')


else:
    print('Bad Cred')
    
a = [1,2,3]
b = [1,2,3]

if a == b:
    print("True")

else:
    print("False")
    
if a is b:
    print("True")
else:
    print("False")
    print(id(a))
    print(id(b))

#
b = a
if a is b:
    print("True")
    print(id(a))
    print(id(b))

else:
    print("False")