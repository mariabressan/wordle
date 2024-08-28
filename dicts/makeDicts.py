import numpy as np

wordLength = 9
allWords = np.loadtxt("scrabbleDict.txt", dtype=str) 

for wordLength in [13,14,15,16,17,18,19,20]:
    f = open(f"scrabble{wordLength}LetterWords.txt", "w")
    for word in allWords:
        if len(word)==wordLength:
            f.write(f"{word.lower()}\n")
    f.close()
