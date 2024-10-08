# List comprehensions 
 

nums = [1,2,3,4,5,6,7,8,9,10]

'''Baiscally list comprehension is easier more readable way'''

# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)

print(my_list)

my_list = [n for n in nums]       #list comprehension
print(my_list)
# I want 'n*n' for each 'n' in nums

my_list = []
for n in nums:
    my_list.append(n*n)
    
print(my_list)

# list compreshension

my_list = [n * n for n in nums]
print(my_list)

# using a map + lambda

my_list = list(map(lambda n:n*n, nums))
print(my_list)

# i want 'n' for each 'n' in nums if 'n' is even
my_list = []
for n in nums:
    if n%2 == 0:
        my_list.append(n)
    
print(my_list)

my_list = list(filter(lambda n: n%2 == 0, nums))
print(my_list)

# I want a (letter, num) pair for each letter in 'abcd' for each number in '0123'

my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))

print(my_list)

#list comperhension

my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(my_list)

# Dictionary Compreshensions
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batsman', 'Superman', 'Spider Man', 'Wolverine', 'Deadpool']

print(dict(zip(names, heros)))

# I want a dict {"name": "hero"} for each name, hero in zip(names, heros)

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

my_dict = {name: hero for name, hero in zip(names, heros) if name != 'peter'}
print(my_dict)


# Set Comprehension
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)

print(my_set)

# Generator Expression 
# I want to yield 'n*n' for each n in nums

# A Generator expression is similar to a list comperhension 

my_gen = (n * n for n in nums)

for i in my_gen:
    print(i)