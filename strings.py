#NOTES from 12/19/2016
#Python Data Structures: Strings

sentence = "Came to Sugarhouse coffee for the first time in months!!"
#Looping with indefinate loop (while)
index = 0
while index < len(sentence):
    letter = sentence[index]
    print letter
    index += 1
#Looping with definite loop (for)
for a in sentence:
    print a
#Count the number of n's
count = 0
for letter in sentence:
    if letter == "n":
        count += 1
    else:
        pass
print "Number of n's = ", count

coffeePosition = sentence.find("coffee")
print coffeePosition

forPosition = sentence.find("for",coffeePosition) #searches from the location of coffeePosition (19)
print forPosition
#Future: Learn dictionaries to do this for every letter

print sentence[5:] #prints from the 5th character to the end of the string sentence
print sentence[:5] #prints from the beginning of the string to the 5th character
print sentence[:] #prints the entire sentence

word = "Sugarhouse    "
print word #print entire word
print word [0] #print first letter
print word[0:4] #print from "s" up to but NOT over "a"
print word[1:4] #print from "u" up to but NOT over "a"
print word [0:1000] #print entire word (no error)

wordLower = word.lower() #makes a letter lowercase
print wordLower

index = word.find('house') #find
print index

dice = word.strip() #strips data from the left and right
print dice

x = 'From marquard@uct.ac.za'
print x[14:17] #print 'utc'

print len(x)*7 #length of the string 'x' multiplied by 7
