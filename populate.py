#!/usr/bin/python

from random import randint as rand
import logging as log
import os 


def populate():
    log.basicConfig(level=log.DEBUG,filename="log_populate",filemode="w")
    prime = ""
    with open("prime","rt") as f:
     prime = f.read()

    log.debug("Prime word is {}".format(prime))
    max_child = 10
    min_child = 5

    numof_child = rand(min_child,max_child)
    log.debug("Number of child is {}".format(numof_child))
    generation = []
    for n in range(numof_child):
        generation.append(prime)
    log.debug("Generation is {}".format(generation))

    with open("generation","w") as f:
        for g in generation:
            f.write(g)
            f.write("\n")


#os.system("./mutate.py")
#os.sys.exit()
