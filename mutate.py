#!/usr/bin/python
import random
import logging as log
import os






gens = list("ABCDEFGHIJKLMNOPRSTUVYZQXW_")
log.basicConfig(level=log.DEBUG,filename="log_mutate",filemode="w")
def mutation():
    

    

    with open("generation","r") as f: # Not-mutated generation is taken 
        pure_generation = f.readlines()
    
    log.debug("Pure generation is {}".format(pure_generation))
    
    
    def mutate(child):
        mutated_child = []
        for l in child:  # For every letter of single child, letter changed randomly with a possiblity of %30
            if random.random() < 0.3 :
                log.debug("Current gen is {}".format(l))
                l = random.choice(gens)
                log.debug("Mutated gen is {}".format(l))
                #breakpoint()
                mutated_child.append(l) # Put together the letters to create mutated child
            else:
                mutated_child.append(l)
        log.debug("mutated_child list is {}".format(mutated_child))
        mutated_child = "".join(mutated_child) 
        log.debug("mutated_child is {}".format(mutated_child))
        return mutated_child
    
    generation = []
    for g in pure_generation:
        g = g.replace("\n","")
        child = mutate(g) # They are mutated at here 
        log.debug("Mutated child is {}".format(child))
        generation.append(child)
    
    log.debug("Mutated generation is {}".format(generation))
    with open("history","a") as f: # They are added to history 
        for g in generation:
            #print(g,file=f,end=" ")
            f.write(g)
            f.write(",")
        f.write("\n")
