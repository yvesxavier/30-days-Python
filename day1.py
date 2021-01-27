# Mehmet SAMUR aka Yves Xavier
#This is easy way to learn Python Day 1.


# Variables & Data Types

character_name = "Yves Xavier"
character_age = "35" # if you store a number you don't need to use "quotation mark"
print("There was a man whose name is " + character_name + "") 
character_name = "Annabel" # changing variables
print(character_name + " is " + character_age + " years old." )

is_male = True
is_female = False #boolean types

# Working with Strings
cool = "Yves Xavier"
print(cool)
print(cool + " is awesome. ") #concatenation
print(cool.lower()) #lovercase
print(cool.upper()) #uppercase
print(cool.isupper()) #Boolean
print(cool.upper().isupper()) #Boolean
print(len(cool)) #length
print(cool[5]) #indexes begin 0
print(cool.replace("Yves","Meth ")) #Replacing items



# Working with Numbers.
from math import *
print(99 % 8) #Modulus operator
print(5 * 99) # change the operator + , - , / * etc. 
print(pow(9,9)) # raised to the power of a number
my_num = 7
print(str(my_num) + " is my lucky number") # changes number to a string.
print(sqrt(49)) # returns us square root

#See you day 2.