from termcolor import colored

colorStrengthDict = {"white":0,"red":1,"yellow":2,"green":3}

def mkList(content,length):
    return [content for i in range(0,length)]

def isvalid(guess,wordBank):
    lenOK = len(guess)==5
    inBank =  "".join(guess) in wordBank
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

def evaluate(guess, answer, wordLength):
    out = ["red" for i in range(0,wordLength)]
    for i,guessLetter in enumerate(guess):
        instances = [i for i, x in enumerate(answer) if x == guessLetter]
        if len(instances) > 0:
            if i in instances:
                out[i] = "green"
            else:
                gMatches = 0
                yMatches = 0
                for instance in instances:
                    if guess[instance] == answer[instance]:
                        gMatches +=1
                ycheck = [i for i, x in enumerate(out) if x == "yellow"]
                for instance in ycheck:
                    if guess[instance] == guessLetter:
                        yMatches+=1
                if len(instances)-gMatches>0 and len(instances)-yMatches>0:
                    out[i] = "yellow"
    return out

def updateAlphabetKey(output,guess,alphabet,alphabetKey):
    for out,letter in zip(output,guess):
        instance = [i for i, x in enumerate(alphabet) if x == letter][0]
        if colorStrengthDict[alphabetKey[instance]] < colorStrengthDict[out]:
            alphabetKey[instance] = out

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