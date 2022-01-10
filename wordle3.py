import os
try :
    dir = '/Users/kanwal/Desktop/Mason/'
    path = dir + 'fiveletterwords.txt'
    print(path)
    f = open(path, 'r')

   #if this isn't working, you need to change directory in terminal to
    # where this file is stored.

    worddict = {}
    lettercount = {}
    wordcount = 0

    for line in f :
        worddict[line.strip()] = 0
        for letter in line:
            if letter in list(lettercount.keys()):
                lettercount[letter] += 1 
            else:
                lettercount[letter] = 1 
        wordcount += 1

except FileNotFoundError: 
    print("Word file not found. Please make sure it's in the same directory as this python file.")
except Exception as e :
    print(e)

letterlist = list(lettercount.keys())
lettersum = sum(list(lettercount.values()))

for letter in letterlist:
    lettercount[letter] = lettercount[letter]/lettersum
print('words analyzed:', wordcount)

# now move on to word analysis

for word in list(worddict.keys()) :
    for letter in word:
        worddict[word] = worddict[word] + lettercount[letter]

# now remove words with reused letters:
for word in list(worddict.keys()):
    curlet = []
    for letter in word:
        if letter in curlet:
            worddict.pop(word)
            break
        curlet.append(letter)

print('words analyzed w/o duplicate letters:', len(list(worddict.keys())))

keymax = max(worddict, key= lambda x: worddict[x])
print(keymax, ':',  worddict[keymax])
