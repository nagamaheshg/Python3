# Numeric  data in python
# type() -  type is built is function in python to find out data type we are used this.
# Integer - Whole Number

num = 20
print(type(num))

# Float - Decimal 
PI =  3.14
print(type(PI))

# Arithmetic operators
'''
    Addition              
    subtraction
    multiplication
    division
    floor division
    exponent
    modulus
'''
print(3 + 2)
print(3 - 2)
print(3 * 3)
print(3 / 2)
print(3 // 2)
print(3 ** 2)
print(3 % 2)

# Increment Operator
num += 1
print(num)

# abs is another built in function remove negative sign return the value
print(abs(-3))

# round is another built in function it round the value near to the number
print(round(3.75, 1)) # round the first digit after decimal

# Comparison Operators
'''
Equal ==
Not Equal !=
Greater than >
Greater than or Equal >=
Less than <
Less than or Equal <=
'''
num_1 = 3
num_2 = 2

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

# Type casting(Explicit type conversion)
# Before Type casting
num_3 = "100"
num_4 = "200"
print(num_3 + num_4)

# After type casting
num_3 = int(num_3)
num_4 = int(num_4)
print(num_3 + num_4)
