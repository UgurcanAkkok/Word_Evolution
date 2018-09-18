#!/usr/bin/python

from random import choice
import logging as log
from os import system

## TODO: takes the Beast as input, writes it to {beast} file 
##       writes prime to {history} file
##       runs {populate}
##       prints how many generations have past

log.basicConfig(level=log.DEBUG, format= "%(asctime)s - %(levelname)s - %(message)s", filename="log_main", filemode="w")

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

system("./populate.py")

log.debug("Program has finished")
