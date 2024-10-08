def square_numbers(nums):
    for i in nums:
        yield (i * i)  

my_nums = square_numbers([1,2,3,4,5])
# print(next(my_nums))
for num in my_nums:
    print(num)
    

my_nums = (x*x for x in [1,2,3,4,5]) # Generator comperhension 
print(list(my_nums))

# Generator better with performance it's not holding all the values 

import memory_profiler
import random
import time

names = ["james", "corey", "Adam", "Steve", "Rick", "Thomas"]
majors = ['Math', 'Engineering', 'Compsci', 'Arts', 'Business']

print(f"Memory (Before): {memory_profiler.memory_usage()[0]} Mb")

def people_list(num_people):
    
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
            
        }
        yield person
        
# t1 = time.perf_counter()
# people = people_list(1000000)
# t2 = time.perf_counter()

        
t1 = time.perf_counter()
people = people_generator(1000000)
t2 = time.perf_counter()

print(f"Memory (After list): {memory_profiler.memory_usage()[0]} Mb")
print(f'Took {t2-t1} seconds')

'''
Key Points:
Memory Efficiency:
A list holds all generated values in memory, so as the number of people increases, memory usage grows.
A generator, on the other hand, only generates values as needed, keeping memory usage low.

Performance:
The list version consumes more memory, and when dealing with large datasets (like 1 million items), this can lead to high memory usage.
The generator version uses significantly less memory, as it doesn’t store all the items at once.
'''