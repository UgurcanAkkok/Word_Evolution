#!/usr/bin/python
import random
import logging as log

log.basicConfig(level=log.DEBUG,filename="log_mutate")

gens = list("ABCDEFGHıJKLMNOPRSTUVYZQXW_")

with open("generation","r") as f:
    pure_generation = f.readlines()

log.debug("Current generation is {}".format(pure_generation))

def mutate(child):
    mutated_child = ""
    for l in child:
        if random.random() < 0.3 :
            l = random.choice(gens)
        mutated_child.join(l)
    return mutated_child

generation = []
for g in pure_generation:
    child = mutate(g)
    log.debug("Mutated child is {}".format(child))
    generation.append(child)

log.debug("Mutated generation is {}".format(generation))
with open("history","w+") as f:
    for g in generation:
        print(g,file=f,end=" ")


