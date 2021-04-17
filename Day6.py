# Mehmet SAMUR aka Yves Xavier
# This is the easy way to learn Python Day6
#Break Statement

username = "myusername"
password = "passw0rd"
while True:
     quest1 = input("username: ")
     quest2 = input("password: ")
     if quest1 == username and quest2 == password:
         print("Success")
         break
     else:
         print("Wrong Username or Password")
         print("Please try again.)
#Continue Statement
while True:
    s = input("Enter a number: ")
    if s == "cancel":
        break
    if len(s) <= 3:
        continue
    print("Enter a 3 digit number. ")


#another example
number = "23430234034340345670234509585609945459954995400000000000009454504500000"
for i in number:
    if i == "0":
        continue
    else:
        print(i)

# In(in) keyword
answer = input("Are you sure wanna quit? [Y/N] ")
if answer in "Y" or "y":
    print("Good bye.")
elif answer in "N" or "n":
    print("Ok buddy.")


#Guessing number Game
import random
numbergame = random.randint(0, 100)
message = "I got a secret number\nCan you guess it?\nPress \"q\" for quit .  "
print(message)
while True:
    guess = input("Enter guess")
    if guess == "q":
        print("Quitting bitch.")
        break
    guess = int(guess)
    if guess == numbergame:
        print("Congrats. number is true.")
        break
    if guess < numbergame:
        print("Enter higher number.")
    elif guess > numbergame:
    else:
        print("C'mon you can do it.")

#this will write letter byYvesXavier letter 'YvesXavier'
#for tdoay this is enough. See you on day 7.
