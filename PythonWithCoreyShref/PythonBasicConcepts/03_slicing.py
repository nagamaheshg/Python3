# slicing strings and list or tuples
#         -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# list[start: end: step]

print(my_list)
print(my_list[0:6])
print(my_list[3:8])
 
print(my_list[-7: -2])
print(my_list[1:-2])

print(my_list[1:]) # getting empty

print(my_list[:])

print(my_list[2: -1])

# default step size is one
print(my_list[2:-1:2])

print(my_list[-1:2:-1]) #printing in reverse order

print(my_list[::-1]) # reverse string or list

# sample url

sample_url = "https://www.google.com"
print(sample_url)

# Reverse the url
print(sample_url[::-1])

#
print(sample_url[-4:])

# print the url without the http://
print(sample_url[8:-4])