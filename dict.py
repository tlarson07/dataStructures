#NOTES from 12/29/2016
#Python Data Structures: Dictionaries

#Dictionaries are a bag of values, each with it's own label
#Associative Array = Key/Value (In python its a dictionaries)

purse = dict()
purse['money'] = 150 #adding key (money) and value (150) to dictionary (purse)
purse['candy'] = "Skittles" #adding key (candy) and value (Skittles) to dictionary (purse)
purse['tissues'] = 3 #adding key (tissues) and value (3) to dictionary (purse)
print purse
print purse['candy'] #print the value for the key (candy)

purse['money'] += 100 #increase the value of money by 100
print purse

purse['money'] = 1000
print purse

sentence = "Here is a simple sentence with few words that I may or may not repeart: apple, pear, apple, pear, apple, pear, apple, pear and pear."


#---------------sentenceToList function---------------
#-----1. Removes special characters from string
#-----2. Makes all characters lowercase
#-----3. Splits sentence (each words becomes an element in a list)
#-----4. Returns string
def sentenceToList(sentence):
    newSentence = ""
    for letter in sentence:
        if letter.isalnum() == True: #if character is a number or letter then the boolean is True
            pass #nothing happens
        elif letter == " ": #if character is a space
            pass #nothing happens
        else:
            continue
        newSentence += letter #addes letter to newSentence
    newSentence = newSentence.lower() #makes each letter lowercase
    newSentence = newSentence.split() #splits the setence based on spaces
    return newSentence

#----------------sentenceToDict function---------------
#-----1. Removes special characters from string
#-----2. Makes all characters lowercase
#-----3. Splits sentence (each words becomes an element in a list)
#-----4. Calculates word frequency using dictionary (key = word, value = frequency)
#-----5. Returns dictionary
def sentenceToDict(sentence):
    newSentence = "" #creates and
    wordDict = {}
    for letter in sentence:
        if letter.isalnum() == True: #if character is a number or letter then the boolean is True
            pass #nothing happens
        elif letter == " ": #if character is a space
            pass #nothing happens
        else:
            continue
        newSentence += letter #addes letter to newSentence
    newSentence = newSentence.lower() #makes each letter lowercase
    newSentence = newSentence.split() #splits the setence based on spaces
    for word in newSentence:
        wordDict[word] = wordDict.get(word,0) + 1 #if NO entry sets value for key (word) as 0, then increase the value by 1
    return wordDict

#----------------sortedDict function---------------
#-----Prints dictionary based on size of value from largest to smallest
def sortedDict(dictionary):
    for i in sorted(dictionary, key=dictionary.get, reverse=True): #sorts dictionary based on size of key from largest to smallest (change "reverse" boolean to False to print from smalles to largest)
        print i, dictionary[i]

#----------------mostCommonWord function---------------
#-----Returns tuple containing most common word + frequency
def mostCommonWord(dictionary):
    largestWord=None #sets largestWord as None
    largestNumber=None #sets largestNumber as None
    for word,frequency in dictionary.items(): #WOWOWOWO Double interation (word,frequency)
        if largestNumber is None or frequency > largestNumber: #if largestNumber = None or frequency is greater then the largestNumber
            largestNumber = frequency #sets frequency as the largestNumber
            largestWord = word #sets word as the largestWord
    return largestWord,largestNumber

dictionary=sentenceToDict(sentence)

sortedDict(dictionary)
print sentenceToDict(sentence).get('pear') #prints the vaule from the key (pear) from the dictionary (sentenceToDicta(sentence))
print list(sentenceToDict(sentence)) #dictionary keys in a list
print sentenceToDict(sentence).keys() #dictionary keys in a list (pt 2)
print sentenceToDict(sentence).values() #dictionary values in a list
print sentenceToDict(sentence).items() #creates list of tuples from a dictionary
print mostCommonWord(dictionary)
