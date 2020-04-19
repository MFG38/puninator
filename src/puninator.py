# The main program of Puninator.

from punlist import puns
import random

lastPun = ""

# givepun(): Picks a pun from the list and stores it
# to the lastPun variable.
def givepun():
    lastPun = random.choice(puns)
    print lastPun

if __name__ == "__main__":
    givepun()

