# Mehmet SAMUR aka Yves Xavier
# This is the easy way to learn python day 4 .


# Dictionaries.

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jul": "July",
    "Jun": "June",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
# you can use this attributes the reach elements.
print(monthConversions["Jan"])
print(monthConversions.get("Nov"))

# While Loop
i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop")

# Building a guessing game

secret_word = "Yves Xavier"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess : ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, You Lose Sucker !!!")
else:
    print("You Win !!!")

# For Loop

for letter in "Yves Xavier":
    print(letter)

friends = ["Jim", "Karen", "Mike", "Meth", "Kevin"]
for friend in friends:
    print(friends)

for index in range(3, 300):
    print(index)  # it will print all the number between 3 and 300

# See you day 5.