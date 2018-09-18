#!/usr/bin/python
import random
import logging as log
from os import system

log.basicConfig(level=log.DEBUG,filename="log_mutate",filemode="w")

gens = list("ABCDEFGHIJKLMNOPRSTUVYZQXW_")

with open("generation","r") as f:
    pure_generation = f.readlines()

log.debug("Pure generation is {}".format(pure_generation))


def mutate(child):
    mutated_child = []
    for l in child:
        if random.random() < 0.3 :
            log.debug("Current gen is {}".format(l))
            l = random.choice(gens)
            log.debug("Mutated gen is {}".format(l))
            #breakpoint()
            mutated_child.append(l)
        else:
            mutated_child.append(l)
    log.debug("mutated_child list is {}".format(mutated_child))
    mutated_child = "".join(mutated_child) 
    log.debug("mutated_child is {}".format(mutated_child))
    return mutated_child

generation = []
for g in pure_generation:
    g = g.replace("\n","")
    child = mutate(g)
    log.debug("Mutated child is {}".format(child))
    generation.append(child)

log.debug("Mutated generation is {}".format(generation))
with open("history","a") as f:
    for g in generation:
        #print(g,file=f,end=" ")
        f.write(g)
        f.write(",")
    f.write("\n")

system("./selection.py")
