# list - a list is a mutiable data type can holde multiple values in single variable
courses = ['History', 'Math', 'Physics', 'Compsci']

# length return number of items in the list
print(len(courses))
print(courses[0])

# Accessing list items by using index value.
print(courses[-1])    # negative -1 return last element form the list or string or tuple

# if your trying to access out of range index you will get list index out of range
# print(courses[4])

# slicing 
print(courses[0:2])
print(courses[2:])

# Add an item to end of the list
courses.append('Art')
print(courses)

# to insert an element specific location we use insert method

courses.insert(1, 'Chemistory')
print(courses)

courses2 = ["GeoScience", "Biology"]
# to added multiple values to list we use extend method

courses.extend(courses2)
print(courses)

# remove items from list
courses.remove('Math')
print(courses)

# Don't do this mistake


# pop return the value that removed
popped = courses.pop()
print(popped)
print(courses)

# reverse the list
courses.reverse()
print(courses)

# sort the list
courses.sort() 
print(courses)

nums = [1, 5, 3, 4, 2]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

# min, max, sum are built in function in python

print(min(nums))
print(max(nums))
print(sum(nums))

# return the index value of item or else return valueError
#print(courses.index('Compsc'))
print("Compsci" in courses)

# enumerate function return index and that value.
for index,item in enumerate(courses):
    print(f'{index+1} | {item}')
print('-------')
for index,item in enumerate(courses, start=1):
    print(f'{index} | {item}')

print('-'*20)
# to convert list items to string by using join method

course_str = (', ').join(courses)
print(course_str)

# split is another method to convert string to list
course_list = course_str.split(', ')
print(course_list)


list_1 = ['History', 'Math', 'Physics', 'Compsci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

# Tuples are similar to list but tuples are immutable data type.

tuple_1 = ('History', 'Math', 'Physics', 'Compsci')
tuple_2 = tuple_1

print(tuple_2)

# we can reassign tuple value.
#tuple_1[0] = 'Art' # tuple object doesn't support item reassignment
print(tuple_1)
print(tuple_2)

# set - set are unordered and also have no duplicates.
# sets remove duplicates

cs_courses = {'History', 'Math', 'Physics', 'CompSci' }
art_courses = {'History', 'Math', 'Art', 'Design'}

# intersection - list out the common courses in both sets
print(cs_courses.intersection(art_courses))
print(cs_courses)

# difference - list out the unique courses in cs_courses list.
print(cs_courses.difference(art_courses))

# union - merge both sets if any duplicate elements its remove and gives unique values in both sets
print(cs_courses.union(art_courses))

# Empty list:

empty_list = []
empty_list = list()

# Empty Tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty set
empty_set = {} #This is not set
# to define empty set
empty_set = set()
