from termcolor import colored

colorStrengthDict = {"white":0,"red":1,"yellow":2,"green":3}

# MISC
def mkList(content,length):
    return [content for i in range(0,length)]

# CHECKING GUESSES
def isvalid(guess,wordBank,wordLength):
    lenOK = len(guess)==wordLength
    inBank =  "".join(guess) in wordBank
    if lenOK and inBank:
        return True

    if not lenOK:
        print("Guess invalid: must be 5 letters")
    elif not inBank:
        print("Guess invalid: word not in bank")
    return False

def evaluate(guess, answer):
    out = ["red" for i in range(0,len(answer))]
    for i,guessLetter in enumerate(guess):
        instances = [i for i, x in enumerate(answer) if x == guessLetter]
        if len(instances) > 0:
            if i in instances:
                out[i] = "green"
    for i,guessLetter in enumerate(guess):
        instances = [i for i, x in enumerate(answer) if x == guessLetter]
        if len(instances)>0 and i not in instances:
            numStrongMatches = len([letter for letter,outColor in zip(guess,out) if colorStrengthDict[outColor]>1 and guessLetter==letter])
            #ycheck = [i for i, x in enumerate(out) if x == "yellow"]
            #for instance in ycheck:
                #if guess[instance] == guessLetter:
                    #yMatches+=1
            #if len(instances)-gMatches>0 and len(instances)-yMatches>0:
            if numStrongMatches<len(instances):
                out[i] = "yellow"
    return out

def updateAlphabetKey(output,guess,alphabet,alphabetKey):
    for out,letter in zip(output,guess):
        instance = [i for i, x in enumerate(alphabet) if x == letter][0]
        if colorStrengthDict[alphabetKey[instance]] < colorStrengthDict[out]:
            alphabetKey[instance] = out


def calcPossibleWords(possibleWords,guess,output):
    for i,[letter, color] in enumerate(zip(guess, output)):
        if color=="green":
            possibleWords = [word for word in possibleWords if word[i] == letter]
        elif color=="yellow" and guess.count(letter)==1:
            possibleWords = [word for word in possibleWords if word[i] != letter and letter in word]
        elif color=="yellow" and guess.count(letter)>1:
            numStrongOccurances = len([i for i,[guessLetter,outColor] in enumerate(zip(guess,output)) if guessLetter==letter and colorStrengthDict[outColor]>1])
            possibleWords = [word for word in possibleWords if word[i] != letter and word.count(letter)>=numStrongOccurances]
        elif color=="red" and guess.count(letter)==1:
            possibleWords = [word for word in possibleWords if letter not in word]
        elif color=="red" and guess.count(letter)>1:
            numStrongOccurances = len([i for i,[guessLetter,outColor] in enumerate(zip(guess,output)) if guessLetter==letter and colorStrengthDict[outColor]>1])
            possibleWords = [word for word in possibleWords if word[i] != letter and word.count(letter)==numStrongOccurances]
    return possibleWords

# PRINTING
def printOutput(guess,output):
    for letter, out in zip(guess,output):
        text = colored(letter, out)
        print(text,end="")
    print()

def printAllOutputs(allOutputs):
    print()
    for guess, output in allOutputs:
        print("      ",end="")
        for letter, out in zip(guess,output):
            print(colored(letter, out),end="")
        print()

def printAlphabetKey(alphabet,alphabetKey):
    print()
    for i in range(0,10):
        print(f"{colored(alphabet[i],alphabetKey[i])} ",end="")
    print("\n ",end="")
    for i in range(10,19):
        print(f"{colored(alphabet[i],alphabetKey[i])} ",end="")
    print("\n  ",end="")
    for i in range(19,26):
        print(f"{colored(alphabet[i],alphabetKey[i])} ",end="")
    print("\n")

def winPrint():
    print('''
██╗░░░██╗░█████╗░██╗░░░██╗  ░██╗░░░░░░░██╗██╗███╗░░██╗██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ░██║░░██╗░░██║██║████╗░██║██║
░╚████╔╝░██║░░██║██║░░░██║  ░╚██╗████╗██╔╝██║██╔██╗██║██║
░░╚██╔╝░░██║░░██║██║░░░██║  ░░████╔═████║░██║██║╚████║╚═╝
░░░██║░░░╚█████╔╝╚██████╔╝  ░░╚██╔╝░╚██╔╝░██║██║░╚███║██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
            ''')
    
def loosePrint(answer):
    print(f'The word was {"".join(answer)}')
    print('''
██╗░░░██╗░█████╗░██╗░░░██╗  ██╗░░░░░░█████╗░░█████╗░░██████╗███████╗  ██╗░░██╗
╚██╗░██╔╝██╔══██╗██║░░░██║  ██║░░░░░██╔══██╗██╔══██╗██╔════╝██╔════╝  ╚═╝░██╔╝
░╚████╔╝░██║░░██║██║░░░██║  ██║░░░░░██║░░██║██║░░██║╚█████╗░█████╗░░  ░░░██╔╝░
░░╚██╔╝░░██║░░██║██║░░░██║  ██║░░░░░██║░░██║██║░░██║░╚═══██╗██╔══╝░░  ░░░╚██╗░
░░░██║░░░╚█████╔╝╚██████╔╝  ███████╗╚█████╔╝╚█████╔╝██████╔╝███████╗  ██╗░╚██╗
░░░╚═╝░░░░╚════╝░░╚═════╝░  ╚══════╝░╚════╝░░╚════╝░╚═════╝░╚══════╝  ╚═╝░░╚═╝
          ''')