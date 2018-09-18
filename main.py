#!/usr/bin/python

from random import choice
import logging as log
import os

## TODO: takes the Beast as input, writes it to {beast} file 
##       writes prime to {history} file
##       runs {populate}
##       prints how many generations have past

log.basicConfig(level=log.DEBUG, format= "%(asctime)s - %(levelname)s - %(message)s", filename="log_main", filemode="w")

log.disable(log.CRITICAL)
with open("beast","w") as f:
    beast = input("Enter the word that will win the evolution.\n>")
    beast = beast.upper().replace(" ","_")
    f.write(beast)


gens = list("ABCDEFGHIJKLMNOPRSTUVYZQXW_")

prime = []
for l in beast:
    prime.append(choice(gens))
prime = "".join(prime)
with open("prime","w") as f:
    f.write(prime)

log.debug("Prime is {}".format(prime))

with open("history","w") as f:
    f.write(prime)
    f.write("\n")

#os.system("./populate.py")

if __name__ == "__main__":
    while True:
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
#log.debug("Program has finished")
#os.sys.exit()
