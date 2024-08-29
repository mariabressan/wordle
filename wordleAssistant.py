import numpy as np

from wordleHelpers import *

### Shows valid solutions given info of guess:output ###

info = {     
    "shine":"ryyrg",               
        }             
               
########################################################

colorDict = {"r":"red","y":"yellow","g":"green"}

possibleWords = np.loadtxt(f"dicts/validWordleWords.txt", dtype=str) 
nTotal = len(possibleWords)
for guess in info:
    output = [colorDict[i] for i in info[guess]]
    possibleWords = calcPossibleWords(possibleWords,guess,output)
nPossible = len(possibleWords)
print(f'{nPossible}/{nTotal}')
print(possibleWords)

