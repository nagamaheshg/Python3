# collections.counter() in python

# Required count number of fruits 

from collections import Counter
fruits = ['Apple', 'Banana', 'Apple', 'Orange','Apple', 'Orange']
fruit_count = Counter(fruits)
print(fruit_count)
# fruit_count  = {fruit: fruits.count(fruit) for fruit in fruits}
# print(fruit_count)

# Not make this mistake in python
# List Tricks in python

elements=['k','L','M','N','O']
for item in elements:
    if item == 'M':
        elements.remove('M')
    else:
        print(item)
        
# Do this improvement of your script. This script taking bit longer

def fibo(n:int) -> int:
    if n <= 1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
for i in range(0, 100):
    print(f'{i} --> {fibo(i)}')
    

# from functools import lru_cache    #lru_cache -> store each call to memory

# @lru_cache
# def fibo(n:int) -> int:
#     if n <= 1:
#         return n
#     else:
#         return fibo(n-1)+fibo(n-2)
    
for i in range(0, 10):
    print(f'{i} --> {fibo(i)}')
