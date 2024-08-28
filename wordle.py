import random
import numpy as np

from wordleHelpers import *

wordLength, numTurns = 5, 6
wordBank = np.loadtxt(f"dicts/scrabble{wordLength}LetterWords.txt", dtype=str) 
possibleWords = wordBank
alphabet = list("qwertyuiopasdfghjklzxcvbnm")
alphabetKey = mkList("white",26)
allOutputs = []

answer = list(random.choice(wordBank))
output = mkList("red",wordLength)
count = 1

print(f"\nRules: Guess a {wordLength}-letter word within {numTurns} turns.")
print(f'{colored("green", "green")}- correct letter, corect spot')
print(f'{colored("yellow", "yellow")} - correct letter, incorrect spot')
print(f'{colored("red", "red")} - incorrect letter\n')

while count<numTurns+1 and output!=mkList("green",wordLength):
    print('answer: ', answer)
    guess = list(input(f"Guess #{count}: ").lower())
    if isvalid(guess,wordBank,wordLength):
        output = evaluate(guess,answer)
        allOutputs.append([guess,output])
        updateAlphabetKey(output,guess,alphabet,alphabetKey)
        possibleWords = calcPossibleWords(possibleWords,guess,output)
        count+=1
    print(f'{len(possibleWords)}/{len(wordBank)} possible words left')
    print("possible words: ",possibleWords)
    printAllOutputs(allOutputs)
    printAlphabetKey(alphabet,alphabetKey)

    if "".join(answer) not in possibleWords:
        print("ERROR answer not in possibleWords")
        exit()

    if output==mkList("green",wordLength):
        winPrint()

    if count > numTurns:
        loosePrint(answer)

