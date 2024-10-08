# loops and iterations

nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
        print("Found!")
        break
    else:
        print(num)

# continue: ignore

for num in nums:
    if num == 3:
        print("Found!")
        continue
    else:
        print(num)
        

# loop inside another loop

for num in nums:
    for letter in 'abc':
        print(f'{num}:{letter}')

for i in range(1, 11):
    print(i)
    
# while loop

x = 0
while x < 10:
    if x == 5:
        break
    print(x)
    x += 1
    
# To create infinite loop

# while True:
