#NOTES 12/31/2016
#Python Data Structures: Tuples

#Similar to lists BUT
#Can't be changed after creation (NO: appending, sorting, reversing, etc.
#Therefore they are more efficient

friends = ("Annalise", "Gigi", "Kepler") #
numbers = (13,6,1,23,7)

print friends[1]
print max(numbers)

(age,name) = (15,"Lauren") #assigning two variables at once
print name
print age

age,name = (15,"Lauren") #assigning two variables at once WITHOUT parathesis
print name
print age

print (18,33,75) > (8,32,2) #tuples are compariable, runs through each element until False, or prints True

#DICTIONARY ----> LIST of TUPLES ----> SORTED LIST
family = {"Lauren":15, "Paige":10, "Tanner":18, "Jennifer":43, "Bruce": 50}
t = family.items() #turns dict (family) into a list of tuples (t)
print t
t.sort() #sorts the list of tuples by keys
print t

#DICTIONARY ----> LIST of SORTED TUPLES
family = {"Lauren":15, "Paige":10, "Tanner":18, "Jennifer":43, "Bruce": 50}
t = sorted(family.items()) #creates sorted list of tuples (key, value pair) from a dictionary
print t

for person, age in sorted(family.items()):
    print person,age


tAge = list() #creates an empty list (tAge)
for person, age in family.items(): #for key/value (person,age) in list of tuples(family)
    tAge.append((age,person)) #append tuple (age,person)
tAge.sort() #sorts list (tAge), where the key is currenty age
print tAge
