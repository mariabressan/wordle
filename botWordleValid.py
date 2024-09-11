import random
import numpy as np
import matplotlib.pyplot as plt

from wordleHelpers import *

# Plays nTimes # of wordle games for each word length with random valid guesses

alphabet = list("qwertyuiopasdfghjklzxcvbnm")
numTurns = 10

numTimes = 100
#wordLengths = [5]
wordLengths = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
avgs = np.zeros(len(wordLengths))
nPossibleWordsDict = {}

for j,wordLength in enumerate(wordLengths):
    nPossibleWordsList = np.zeros((numTimes,numTurns+1))
    wordBank = np.loadtxt(f"dicts/scrabble{wordLength}LetterWords.txt", dtype=str) 
    counts = np.zeros(numTimes)
    for i in range(numTimes):
        possibleWords = wordBank
        alphabetKey = mkList("white",26)
        allOutputs = []

        answer = list(random.choice(wordBank))
        output = mkList("red",wordLength)
        count=1
        nPossibleWordsList[i][0] = 1

        while output!=mkList("green",wordLength) and count<=numTurns:
            guess = list(random.choice(possibleWords))
            output = evaluate(guess,answer)
            allOutputs.append([guess,output])
            updateAlphabetKey(output,guess,alphabet,alphabetKey)
            possibleWords = calcPossibleWords(possibleWords,guess,output)
            #printOutput(guess,output)
            #print(f"{len(possibleWords)}/{len(wordBank)} words possible")
            if "".join(answer) not in possibleWords:
                print("ERROR answer not in possibleWords")
                exit()
            nPossibleWordsList[i][count] = len(possibleWords)/len(wordBank)
            count+=1
        counts[i] = count

    plt.plot(range(0,numTurns+1),np.mean(nPossibleWordsList,axis=0),label=f"{wordLength}-letter word")
            
    avgs[j] = np.mean(counts)
    print(f"Average # guesses for {wordLength}-letter word is {avgs[j]}")

plt.yscale("log")
plt.title("frac. possible words left after each guess")
plt.legend()
plt.xlabel("# guesses")
plt.show()

'''plt.scatter(wordLengths,avgs)
plt.title("Avg # guesses for x-letter word")
plt.xlabel("# letters in word")
plt.ylabel("Avg # guesses")
#plt.show()'''