# word list taken from https://eslforums.com/5-letter-words/

import os
try :
    dir = '/Users/kanwal/Desktop/Mason/'
    path = dir + 'fiveletterwords.txt'
    print(path)
    f = open(path, 'r')

    #if this isn't working, you need to change directory in terminal to
    # where this file is stored.

    lettercount = {}
    wordcount = 0
    for line in f :
        for letter in line:
            if letter in list(lettercount.keys()):
                lettercount[letter] += 1 
            else:
                lettercount[letter] = 1 
        wordcount += 1

    print('------------ Results ------------')

    letterlist = list(lettercount.keys())
    letterlist.sort()
    for letter in letterlist:
        print(letter, lettercount[letter])

    print('words analyzed:', wordcount)
    print('---------- Results End ----------')

except FileNotFoundError: 
    print("Word file not found. Please make sure it's in the same directory as this python file.")
except Exception as e :
    print(e)
