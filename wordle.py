import random
import numpy as np

from wordleHelpers import *

wordBank = np.loadtxt("dicts/validWordleWords.txt", dtype=str) 
alphabet = list("qwertyuiopasdfghjklzxcvbnm")
alphabetKey = mkList("white",26)
wordLength = 5
numTurns = 6
allOutputs = []

answer = list(random.choice(wordBank))
output = mkList("red",wordLength)
count = 1

print(f"\nRules: Guess a {wordLength}-letter word within {numTurns} turns.")
print(f'{colored("green", "green")}- correct letter, corect spot')
print(f'{colored("yellow", "yellow")} - correct letter, incorrect spot')
print(f'{colored("red", "red")} - incorrect letter\n')

while count<numTurns+1 and output!=mkList("green",wordLength):
    guess = list(input(f"Guess #{count}:\n"))
    if isvalid(guess,wordBank):
        output = evaluate(guess,answer,wordLength)
        allOutputs.append([guess,output])
        printAllOutputs(allOutputs)
        updateAlphabetKey(output,guess,alphabet,alphabetKey)
        printAlphabetKey(alphabet,alphabetKey)
        count+=1

    if output==mkList("green",wordLength):
        winPrint()

    if count > numTurns:
        loosePrint(answer)

