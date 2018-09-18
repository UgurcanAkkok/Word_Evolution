#!/usr/bin/python
from random import choice 
import logging as log
import os


temp_file = open("ancestors","w")
temp_file.close()

def selection():
    log.basicConfig(level=log.DEBUG, filename="log_selection", filemode="w")
    generation = []
    str_generation = ""
    with open("history","r") as f_history:
        history = f_history.readlines()
        str_generation = history[-1]
        generation = str_generation.strip("\n").split(",")
        generation = generation[:-1]
        log.debug("Generation is {}".format(generation))
    
    beast = ""
    with open("beast","r") as f:
        beast = f.read()
    
    def select(generation):
        score_gens = []
        score_scores = []
        score_table = []
        for gen in generation:
            score = 0
            count = 0
    
            for letter in gen:
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
        highest = score_scores[0]
        finalists = []
        for item in score_table:
            if item[1] == highest:
                log.debug("Score table item:{}".format(item))
                finalists.append(item[0])
            else:
                continue
        log.debug("Finalists are {}".format(finalists))
        
        winner = choice(finalists)
        with open("ancestors","a") as f:
            f.write(winner)
            f.write("\n")
        with open("prime","w") as f:
            f.write(winner)
        #breakpoint()
        return winner
    
    winner = select(generation)
    if winner == beast:
        print("One person became beast!!")
    #if winner != beast:
     #   os.system("./populate.py")
      #  os.sys.exit()
    #else:
     #   print("One person has evolved to the beast!!")
      #  input("Remove {ancestors} file")
       # os.sys.exit()
