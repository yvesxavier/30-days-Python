# Mehmet SAMUR aka Yves Xavier
#This is easy way to learn Python Day 2.


# Getting Input From Users.
name = input("Enter your name: ")
print("Hello " + name + "," )

# Building Basic Calculator:
num1 =  input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) - int(num2) # operator changeable
print(result)  # using decimal numbers give an error.


# Madlib Game
adjective = input("Enter an adjctive: ")
adjective2 = input("Enter another adjctive: ")
type_of_bird = input("Enter a bird type: ")
room_in_a_house = input("Enter a room in a house: ")
past_tense_verb = input("Enter a past tense verb: ")
print("It was a " + adjective + " , cold November day. I woke up to the "  + adjective2 + " smell of " + type_of_bird + " roasting in the " + room_in_a_house + " downstairs. I " + past_tense_verb + " down the stairs to the ...." )

# Lists
friends = ["Meth"  ,"Matthew" , "Kylie" , "Irem" , "Xavier" , "Yves"]
print(friends[3])
print(friends[1:]) # select index 1 and then.
friends[3] = "Fatma" #changes Irem to Fatma.

# List Functions.
lucky_numbers = [ 4 , 8 , 15 , 16 , 23 , 42  ]
friends = ["Meth"  ,"Matthew" , "Kylie" , "Irem" , "Xavier" , "Yves"]
friends.extend(lucky_numbers) # it will extend lucky_numbers to friends.
friends.append("Fatma") # It will append Fatma to frinds
friends.insert(1 , "Kelly") # It will insert Kelly to index 1.
friends.remove("Kylie") #removes the input.
friends.pop() #if it's blank, removes the last item. if you add index removes the index's item.
friends.sort() #It will give an alphabetical order.
friends2 = friends.copy # makes a copy of the friends and we can set up everything with copied value.
print(friends2)

# See you day 3