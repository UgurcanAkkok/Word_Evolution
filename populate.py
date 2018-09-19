#!/usr/bin/python

from random import randint as rand
import logging as log
import os 




min_child = 5
max_child = 20
log.basicConfig(level=log.DEBUG,filename="log_populate",filemode="w")
def populate():
    
    prime = ""
    with open("prime","rt") as f: # Reads prime
     prime = f.read()

    log.debug("Prime word is {}".format(prime))
    
    

    numof_child = rand(min_child,max_child) # Childs are generated between the numbers of the 10 and 5, can easily change
    log.debug("Number of child is {}".format(numof_child))
    generation = []
    for n in range(numof_child): # Simply copy-paste prime so that mutate() can easily mutate them
        generation.append(prime)
    log.debug("Generation is {}".format(generation))

    with open("generation","w") as f: # Saves generated generation to file
        for g in generation:
            f.write(g)
            f.write("\n")
