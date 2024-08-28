import numpy as np
import random
import matplotlib.pyplot as plt

nGames = 100
nGuesses = [random.randint(1, 100) for _ in range(nGames)]


printout = [np.mean(nGuesses[int(np.linspace(0,nGames,11)[x]):int(np.linspace(0,nGames,11)[x+1])]) for x in range(0,10)]

plt.scatter(nGuesses,range(0,nGames))
plt.show()
print(printout)