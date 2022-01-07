
import random


def wordlegame(guess, WORDLE, resultdict = {'CORRECT' : [], 'WRONG' : [], 'MOVE' : []}):

    resultstr = []
    guess = list(guess)
    wordle = list(WORDLE)

    for i in range(len(wordle)):
        if guess[i] == wordle[i]:
            resultstr.append(guess[i])
            if not(guess[i] in resultdict['CORRECT']):
                resultdict['CORRECT'].append(guess[i])
        elif guess[i] in wordle:
            resultstr.append('_')
            if not ((guess[i] in resultdict['CORRECT']) or (guess[i] in resultdict['MOVE'])):
                resultdict['MOVE'].append(guess[i])
        else:
            resultstr.append('_')
            if not((guess[i] in resultdict['CORRECT']) or (guess[i] in resultdict['WRONG']) or (guess[i] in resultdict['MOVE'])):
                resultdict['WRONG'].append(guess[i])

    return resultdict, resultstr

# import the wordle list
try :
    dir = '/Users/kanwal/Desktop/Mason/'
    path = dir + 'fiveletterwords.txt'
    print(path)
    f = open(path, 'r')
except FileNotFoundError: 
    print("Word file not found. Please make sure it's in the same directory as this python file.")
except Exception as e :
    print(e)

posswords = []
for line in f:
    posswords.append(line)

WORDLE = random.sample(posswords, 1)[0].strip()
WIN = False
guesses = []

print('------------ Begin Game ------------')

att = 1

while WIN == False : 

    goodinput = False
    while goodinput == False:
        try: 
            txt = str(att) + '. ' + 'What is your guess? Type in 5 letters and hit ENTER: '
            guess = input(txt).lower()
            if len(guess) != 5 or any(map(str.isdigit, guess)): 
                raise ValueError
            else: 
                goodinput = True
        except ValueError :
            print('Please try again.')

    resultdict, resultstr = wordlegame(guess, WORDLE)
    print('       ------>', ' '.join(resultstr), '<------')
    print(resultdict)
    print()
    att += 1

    if  ''.join(resultstr) == WORDLE:
        print ('You got the wordle in', att-1, 'tries! Congrats!')
        WIN = True
        print('------------- End Game -------------')
        print('The word was:', WORDLE)
    
    if att > 6:
        print ('You are out of tries.')
        WIN = True
        print('------------- End Game -------------')
        print('The word was:', WORDLE)




