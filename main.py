#!/usr/bin/python

from random import choice
import logging as log
from os import system

## TODO: takes the Beast as input, writes it to {beast} file 
##       writes prime to {history} file
##       runs {populate}
##       prints how many generations have past

log.basicConfig(level=log.DEBUG, format= "%(asctime)s - %(levelname)s - %(message)s", filename="log_main")

f_beast = open("beast","w")
f_prime = open("prime","w")
f_history = open("history","w") 

beast = input("Enter the word that will win the evolution.\n>")
beast = beast.replace(" ","_")
print(beast, file=f_beast)
gens = list("ABCDEFGHIJKLMNOPRSTUVYZQXW_")

prime = []
for l in beast:
    prime.append(choice(gens))
prime = "".join(prime)
print(prime,file=f_prime)
print(prime,file=f_history)

system("./populate.py")

while True:
    try:
        history = open("history","r")
    except FileNotFoundError:
        continue


length = len(history.readlines())
print(f"{length} generations have past to reach the final state.")
f_beast.close()
