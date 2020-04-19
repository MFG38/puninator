# The main program of Puninator.

from punlist import puns
import random

def givepun():
    punindex = random.randint(0,len(puns)-1)
    heresapun = puns[punindex]
    print heresapun

if __name__ == "__main__":
    givepun()

