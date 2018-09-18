#!/usr/bin/python

from random import choice
import logging as log
import os

## Takes beast as goal of evolution, then creates a primal creature, runs functions from other files that needed.
#### TODO: Reduce the unneccasarily repeated action, there is too much of them
####           Things under OPERATION.OPERATION() function
####           Imports under while loop in {main}
####       Put a config file to change evolution settings
log.basicConfig(level=log.DEBUG, format= "%(asctime)s - %(levelname)s - %(message)s", filename="log_main", filemode="w")

log.disable(log.CRITICAL)
with open("beast","w") as f: # Define beast and TODO check it if it has non-available chars
    beast = input("Enter the word that will win the evolution.\n>")
    beast = beast.upper().replace(" ","_")
    f.write(beast)


gens = list("ABCDEFGHIJKLMNOPRSTUVYZQXW_")

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

#os.system("./populate.py")

if __name__ == "__main__":
    while True: # Populate, mutate them, eliminate them, check if someone reached the beast
        import populate 
        populate.populate()
        import mutate
        mutate.mutation()
        import selection
        selection.selection()
        with open("prime", "r") as f:
            ancestor = f.read()
            if ancestor == beast :
                break
            else:
                continue
    print("Hey i think someone reached final state")
