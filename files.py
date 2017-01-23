#NOTES from 12/22/2016
#Python Data Structures: Files

#Handle method to read the data (an access center)
f = open("data.txt") #opens the file data.txt in read mode ('r') vs write mode ('w')
contentWhole = f.read() #puts the content of the file in a single string, punctuating newlines with '\n'
contentLine = f.readlines() #puts each line of a the file in a string ending with '\n' THEN each string is added to a list
print f, "\n"
print contentWhole

sentence1 = "Came to Sugarhouse coffee for the first time in months!!"
sentence2 = "Came\nto\nSugarhouse\ncoffee\nfor\nthe\nfirst\ntime\nin\nmonths!!"
print sentence1 + "\n"
print sentence2 + "\n"
print len(sentence1),"\n" #prints the length of sentence1
print len(sentence2),"\n" #prints the length of sentence2 (SAME AS SENTENCE 1)

#BROKEN PIPE: Open files befoer each loop
tinyF = open('data.txt')
count = 0
for line in tinyF:
    line = line.rstrip('\n') #removes the "\n" from each line
    count += 1
print count

print "\n"
tinyF = open('data.txt')
for line in tinyF:
    line = line.rstrip('\n') #removes the "\n" from each line
    if line[0:4] == "From": #if the first four character of the string are "From"
        print line

print "\n"
tinyF = open('data.txt')
for line in tinyF:
    line = line.rstrip()
    if not '@gmail.com' in line: #if the string does NOT contain "@gmail.com"
        continue
    print line
