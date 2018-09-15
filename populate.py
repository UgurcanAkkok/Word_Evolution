#!/usr/bin/python

from random import randint as rand
import logging as log
from os import system 

log.basicConfig(level=log.DEBUG,filename="log_populate")

f_generation = open("generation","w")
f_prime = open("prime","w")
f_history = open("history","w+")

prime = f_prime.read()
log.debug("Prime word is {}".format(prime))
max_child = 10
min_child = 2

numof_child = rand(min_child,max_child)
log.debug("Number of child is {}".format(numof_child))
generation = []
for n in range(numof_child):
    generation.append(prime)
log.debug("Generation is {}".format(generation))
for g in generation:
    print(g,file=f_generation, end=" ")

system("./mutate.py")
