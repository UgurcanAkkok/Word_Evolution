#!/usr/bin/python

from random import choice
import logging as log
from time import process_time as pt

## Takes beast as goal of evolution, then creates a primal creature, runs functions from other files that needed.
####TODO Put a config file to change evolution settings
log.basicConfig(level=log.DEBUG, format= "%(asctime)s - %(levelname)s - %(message)s", filename="log_main", filemode="w")

log.disable(log.CRITICAL)
gens = list("ABCDEFGHIJKLMNOPRSTUVYZQXW_")
with open("beast","w") as f: # Define beast and checks it if it has non-available chars
    beast = input("Enter the word that will win the evolution.\n>")
    pt()
    beast = beast.upper().replace(" ","_")

    for l in beast:
        if (l not in gens):
            raise ValueError("Please use english characters")
    f.write(beast)



prime = []
for l in beast: # Randomly generates prime in the length of beast
    prime.append(choice(gens))
prime = "".join(prime)
with open("prime","w") as f: # Writes prime to a file
    f.write(prime)

log.debug("Prime is {}".format(prime))

with open("history","w") as f: # Startes history with primal creature
    f.write(prime)
    f.write("\n")

if __name__ == "__main__":
    import populate 
    import mutate   
    import selection
    while True: # Populate, mutate them, eliminate them, check if someone reached the beast
        populate.populate()
        mutate.mutation()
        selection.selection()
        with open("prime", "r") as f:
            ancestor = f.read()
            if ancestor == beast :
                break
            else:
                continue
    print("Hey i think someone reached final state")
    print("Program finished it's job in {} time".format(pt()))
