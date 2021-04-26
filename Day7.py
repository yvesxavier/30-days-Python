
#This is Day7, we'll write a little word analyses program for instance.
#Word Analyses program
word = input("Enter the word")
lenght1= len(word)
letter = ""

for letters in word:
    if letter not in letters:
        letters += letter

frequency = ""

for h in letters:
    counters = 0
    for k in word:
        if h == k:
            counters += 1
    frequency += f"\n\t\t{h} letter {counters} time/times. "
print("\n*************************\n")
print(f"\tword has {lenght1}  letter. ")
print("\tword" , end="")
print(*letters , sep="," , end="")
print("has letters. ")
print("\tin letter: ")
print(frequency)
print("\n***************************\n")


#Dictionaries
city = {
    "London" : "snowy" ,
    "Berlin" : "Rainy" ,
    "Istanbul" : "Sunny" ,

}
for k, v in city.items():
    print(f" {k} = {v}")

print(city.items())

#Let's make a little weather program

question = input("Enter a city:")
answer = {
    "London" : "snowy" ,
    "Berlin" : "Rainy" ,
    "Istanbul" : "Sunny" ,

}
print(answer.get(question , f"Weather of this city: No city found."))



#Clusters.

word = input("word: ")
li = []
for letter in word:
    if letter not in li:
        li.append(letter)

print(li)

#shortcut or easy way
word = input("word: ")
cluster = set(word)
print(cluster)

list = set()
l = ["Mehmet" , "Sena" , "Melike" , "Tuğçe" , "Fatma" , "Funda" , "Başak" ,"Aysel" , "Alexandra" , "Nadya" , "Merve"   ]
for items in l:
    list.add(items)
print(list)

list.remove("Merve")
print(list)
list.discard("Nadya") #same with remove method but more comfortable
print(list)

list2 = ["Jim " ,"karen" ,"Tim" ,"David" , "Jacop", "Anastasia" , "Eliot" , "Finch"   ]
list3 = list.update(list2)
print(list3)

#Union
lista = {"A" , "B", "C" }
listb = {"a" ,  "b" , "c" , "D" ,"E" "e"  }
listc = lista.union(listb)
print(listc)
#Difference
listd = lista.difference(listb)
print(listd)

#See you day 8.