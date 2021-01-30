# Mehmet SAMUR aka 'Yves Xavier'
# This is easy way to learn python Day 3.

# Tuples
# Tuples are unique elements and unchangeable

coorditanes = (4,5)
coordinates[1] = 10
print(coorditanes)
'''
It will give an error, using square paranthesis make them Tuples,
if you wanna create a list use open-close paranthesis.
Using square paranthesis out of the Tuples it allows us to change Tuples

'''
coordinates = [(1,3) , (5,90) , (5,7) , (9,6) , (4,8) , (15,16) , (23,42)]
coordinates[1] = 3,7 #It allows us to change index 1.
print(coordinates)

#Functions

def name():
    print(name + " Hello")

# Return Statement

def cub(num):
    return num*num*num
print(cub(9))

# If Statements.

is_male : False
if is_male:
    print("You are a male.")
else:
    print("You are a female.")

#If Statements & Comparisons
def max_num(num1 , num2 , num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(999,88989,9997))

# See you Day 4.























