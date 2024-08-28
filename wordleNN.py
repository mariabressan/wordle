import numpy as np
import math
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras import layers, models
import random

from wordleHelpers import *

'''
Two initial approaches: 
1. Given the current state, which guess reduces the #possible words the most
2. After running a game, each solution is given the same score, which has to do with the # of guesses it took
'''

wordLength, numTurns = 5, 50
nGames = 1000
#wordBank = np.loadtxt(f"dicts/scrabble{wordLength}LetterWords.txt", dtype=str) 
wordBank = np.loadtxt(f"dicts/scrabble{wordLength}LetterWords.txt", dtype=str) 
nTotalWords=len(wordBank)
nGuesses=np.zeros(nGames)

input_shape = (26, wordLength)
NNinput = np.zeros(input_shape)
numCategories = len(wordBank)

model = models.Sequential([
    layers.Flatten(input_shape=input_shape),
    layers.Dense(64, activation='relu'),
    layers.Dense(32, activation='relu'),
    layers.Dense(numCategories, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.3),
              loss='categorical_crossentropy')
for i in range(nGames):
    ansstr = random.choice(wordBank)
    answer = list(ansstr)
    output = mkList("red",wordLength)
    count = 1
    X_sample = np.zeros((1, 26, 5))
    possibleWords = wordBank
    nPossibleWords = len(possibleWords)
    alphabetKey = mkList("white",26)
    allOutputs = []

    while count<numTurns+1 and output!=mkList("green",wordLength) and nPossibleWords!=1:
        nPrevPossibleWords = len(possibleWords)
        #print(f"X_sample = {X_sample}")
        predicted_probs = model.predict(X_sample)
        #print(f"{predicted_probs=}")
        predicted_category = np.argmax(predicted_probs)
        guess = wordBank[predicted_category]
        #print(f"Ans = {ansstr}, Predicted {guess} ({predicted_category})")

        output = evaluate(guess,answer)
        allOutputs.append([guess,output])
        possibleWords = calcPossibleWords(possibleWords,guess,output)
        nPossibleWords = len(possibleWords)
        count+=1
        #score = float(1-(len(possibleWords)/len(wordBank)))
        if (nPrevPossibleWords==1 and guess!=ansstr) or nPossibleWords==nPrevPossibleWords:
            score = 0
        elif guess==ansstr:
            score = 1
        else:
            score = float(math.log(nPossibleWords/nPrevPossibleWords)/math.log(1/nPrevPossibleWords))
        #printOutput(guess,output)
        #print(f"{nPossibleWords}/{nPrevPossibleWords}/{nTotalWords}, score = {score}")
        X_sample = updateXsample(X_sample,guess,output)

        target = np.zeros((1, numCategories))
        target[0, predicted_category] = score
        model.fit(X_sample, target, epochs=1, verbose=0)

    printAllOutputs(allOutputs)
    if output!=mkList("green",wordLength) and count!=numTurns+1:
        print(f"last word was {possibleWords} ",end="")
    else:
        count-=1
    print(f"in {count} guesses")
    nGuesses[i]=count

printout = [np.mean(nGuesses[int(np.linspace(0,nGames,11)[x]):int(np.linspace(0,nGames,11)[x+1])]) for x in range(0,10)]
print(printout)
plt.scatter(range(0,10),printout)
plt.show()
