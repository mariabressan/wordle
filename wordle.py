import numpy as np
from termcolor import colored, cprint
import random

word_bank = np.loadtxt("valid-wordle-words.txt", dtype=str) 

def isvalid(guess):
    lenOK = len(guess)==5
    inBank =  "".join(guess) in word_bank
    lowercaseWord = "".join(guess).islower()
    if lenOK and inBank and lowercaseWord:
        return True

    if not lenOK:
        print("Guess invalid: must be 5 letters")
    elif not lowercaseWord:
        print("Guess invalid: must be a lower case word")
    elif not inBank:
        print("Guess invalid: word not in bank")
    return False

def printoutput(guess,output):
    for letter, out in zip(guess,output):
        if out == "r":
            color = "red"
        elif out == "g":
            color = "green"
        else:
            color = "yellow"
        text = colored(letter, color)
        print(text,end="")
    print()

def evaluate(guess, answer):
    out = list("rrrrr")
    for i,guessLetter in enumerate(guess):
        instances = [i for i, x in enumerate(answer) if x == guessLetter]
        if len(instances) > 0:
            if i in instances:
                out[i] = "g"
            else:
                gMatches = 0
                yMatches = 0
                for instance in instances:
                    if guess[instance] == answer[instance]:
                        gMatches +=1

                ycheck = [i for i, x in enumerate(out) if x == "y"]
                for instance in ycheck:
                    if guess[instance] == guessLetter:
                        yMatches+=1
                if len(instances)-gMatches>0 and len(instances)-yMatches>0:
                    out[i] = "y"
    return out

answer = list(random.choice(word_bank))
output = list("rrrrr")
count = 1

green = colored("green", "green")

print("\nRules: Guess a 5-letter word within 6 turns.")
print(f'{colored("green", "green")}- correct letter, corect spot')
print(f'{colored("yellow", "yellow")} - correct letter, incorrect spot')
print(f'{colored("red", "red")} - incorrect letter\n')

while count<7 and output!=list("ggggg"):
    guess = list(input(f"Guess #{count}:\n"))
    if isvalid(guess):
        output = evaluate(guess,answer)
        printoutput(guess, output)
        count+=1

    if output==list("ggggg"):
        print("Correct, you win!")

if count == 7:
    print(f'Too bad, you lost! The word was {"".join(answer)}')

