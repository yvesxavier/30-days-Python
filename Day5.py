# Mehmet SAMUR aka Yves Xavier
# This is the easy way to learn Python Day5


# Exponent Function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * pow_num
    return result
print(raise_to_power(2,3))
name = "Yves Xavier"
for meth in name:
    print(meth)


#using attribute of for will write "Yves Xavier" letter by letter.
#but if we change like this
for met in name:
    print(name)

#using attribute of name  will write "Yves Xavier" as much as the sum of letters.
numbers = "123456789"

print("base number \tpow number \t\tcubes")
print("----------- \t---------- \t\t-----")
a = 0
while a < 100:
    a += 1
    print(f"{a}\t\t\t\t\t{a ** 2}\t\t\t{a ** 3} ")


#Loops - While Loops
#Loops provide our codes continuity.
while True:
    print("Hey There")
number = 0

while number < 100:
    number += 1
    print(number)
status = 'continue'

while status == 'continue':
    question = input("Enter a data:")
    print(question)
    if question == 'q':
        status = 'enough'
question = input("Python or C++? :")

while question != 'Python':
    print("Wrong Answer.")

#if Loops.
question = input("Python or C++? :")

if question != 'Python':
    print("Wrong Answer.")
status = 'continue'

while status == 'continue':
    question = input("Enter a Data: ")
    print(question)
    if question == "q":
        status = 'enough'
        print("Thanks.")
question = ''


while question != 'q':
    question = input("Enter a data: ")
    print(question)


#For Loops.
numbers = '0123456789'
print(*str(numbers), sep="\n" )


#we can code this like this
for number in str(numbers):
    print(number)


#one more example
for letter in "YvesXavier":
    print(letter)

#this will write letter by letter 'YvesXavier'
#for today this is enough. See you on day 6.