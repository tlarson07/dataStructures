#Notes from 12/24/2016
#Python Data Structures Lists

#Lists are a linear collection of values that stay in order

myFirstList = ["Lauren", [12], 4.7] #lists can be mixed data types
myFirstList[1] = 12 #changed the second element in the 'myFirstList' to 12
print myFirstList[1] #prints the second element in the list
print len(myFirstList) #prints the number of elements in the list
print range (10) #prints 0 through 9
print range(len(myFirstList)) #prints 0 through 2 because there are three iteams in 'myFirstList'
for i in myFirstList: #iterating through lists
    print i

a = [21,2365,23,47,2,8,2]
b = [1,35,1,67,236,7]
c = a + b #concatating lists
print c
c.sort() #sorting list
print c
c.reverse() #reverse the order of the list
print c
dice = c[1:4] #print part of a list
print dice
average = sum(c)/len(c)
print average

stuff = list() #creates an empty list (Alternative: "[]")
stuff.append(10) #addes 10 to the list
stuff.append("Lauren") #addes Lauren to the list
print stuff

sentence = 'Some of my slomies are Brian, Josue, Rebekah, Ginannina, Marcos, Michael, Cami, Danielle, Ben'
def removeSpecialChars(sentence):
    newSentence = ""
    for letter in sentence:
        if letter.isalnum() == True: #if character is a number or letter then the boolean is True
            pass #nothing happens
        elif letter == " ": #if character is a space
            pass #nothing happens
        else:
            continue
        newSentence = newSentence + letter #addes letter to newSentence
    return newSentence

start = removeSpecialChars(sentence).find("Brian") #find the position of Brian in newSentence
slomies = removeSpecialChars(sentence)[start:] #string from brian to end of string
slomiesList = slomies.split() #splits the string based on spaces
print slomiesList

utah = "Mormans;snow;skiing;moochies;cafe-rio"
utahSplit = utah.split(";") #spliting the string based on a character rather than spaces
print utahSplit

f = open("mbox-short.txt")
emails = []
hostNames = []
usernames = []
for line in f:
    line = line.strip() #removes spaces from the left and right sides
    if not line.startswith("From"):
        continue
    words = line.split() #splits line based on spaces and places each substring inside a list
    email = words[1]
    emails.append(email)
for i in emails:
    words = i.split("@") #split based on "@"
    username = words[0]
    hostName = words[1] #puts the second element from the list words in variable, doemainName
    hostNames.append(hostName) #addes hostName to hostNames
    usernames.append(username)
print emails
print usernames
print hostNames

def listOfNumbers():
    numbers = list() #create an empty list
    while True: #while True
        number = raw_input("Please enter a number: ")
        try:
            number = float(number) #if number can be converted to a float
        except:
            break
        numbers.append(number) #add number to list, numbers
    return numbers

numbers = listOfNumbers()
print numbers
average = sum(numbers)/len(numbers)
print average
