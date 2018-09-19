#!/usr/bin/python
from random import choice 
import logging as log
import os

temp_file = open("ancestors","w")
temp_file.close()





log.basicConfig(level=log.DEBUG, filename="log_selection", filemode="w")
def selection():
    
    generation = []
    str_generation = ""
    with open("history","r") as f_history: # Last entry of history is taken as generation
        history = f_history.readlines()
        str_generation = history[-1]
        generation = str_generation.strip("\n").split(",")
        generation = generation[:-1]
        log.debug("Generation is {}".format(generation))
    
    beast = ""
    with open("beast","r") as f: # Beast is taken from the file
        beast = f.read()
    
    def select(generation):
        score_gens = []
        score_scores = []
        score_table = []
        for gen in generation:
            score = 0
            count = 0
    
            for letter in gen: # If letters are the same in the same position, score has ascended 1 point
                if gen[count] == beast[count]:
                    score +=1
                count +=1
                assert count <= len(beast)
            score_gens.append(gen)
            score_scores.append(score)
            score_table.append((gen,score))
        log.debug("Score table is {}".format(score_table))
        log.debug("Scores are :{}".format(score_scores))
        log.debug("Words are :{}".format(score_gens))
    
        score_scores.sort(reverse=True)
        highest = score_scores[0] # Winner's score has chosen
        finalists = []
        for item in score_table: # If chosen score and child's score are the same, child is placed to finalist's position
            if item[1] == highest:
                log.debug("Score table item:{}".format(item))
                finalists.append(item[0])
            else:
                continue
        log.debug("Finalists are {}".format(finalists))
        
        winner = choice(finalists) # Winner chosen from the finalist randomly
        with open("ancestors","a") as f: # Winner ancestor are saved to a file
            f.write(winner)
            f.write("\n")
        with open("prime","w") as f:
            f.write(winner)
        #breakpoint()
        return winner
    
    winner = select(generation)
    if winner == beast:
        print("One person became beast!!")
