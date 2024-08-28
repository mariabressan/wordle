import random
import numpy as np
import matplotlib.pyplot as plt

from wordleHelpers import *

# Plays nTimes # of wordle games for each word length with random valid guesses

alphabet = list("qwertyuiopasdfghjklzxcvbnm")
numTurns = 6

numTimes = 1000
wordLengths = [2,3,4,5,6,7,8,9,10,11,12,13,14,15]
avgs = np.zeros(len(wordLengths))

for j,wordLength in enumerate(wordLengths):
    wordBank = np.loadtxt(f"dicts/scrabble{wordLength}LetterWords.txt", dtype=str) 
    counts = np.zeros(numTimes)
    for i in range(numTimes):
        possibleWords = wordBank
        alphabetKey = mkList("white",26)
        allOutputs = []

        answer = list(random.choice(wordBank))
        output = mkList("red",wordLength)
        count=1

        while output!=mkList("green",wordLength):
            guess = list(random.choice(possibleWords))
            if isvalid(guess,wordBank,wordLength):
                output = evaluate(guess,answer)
                allOutputs.append([guess,output])
                updateAlphabetKey(output,guess,alphabet,alphabetKey)
                possibleWords = calcPossibleWords(possibleWords,guess,output)
                count+=1

            if "".join(answer) not in possibleWords:
                print("ERROR answer not in possibleWords")
                exit()
            
        counts[i] = count
    avgs[j] = np.mean(counts)
    print(f"Average # guesses for {wordLength}-letter word is {avgs[j]}")

plt.scatter(wordLengths,avgs)
plt.title("Avg # guesses for x-letter word")
plt.xlabel("# letters in word")
plt.ylabel("Avg # guesses")
plt.show()