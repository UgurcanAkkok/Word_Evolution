#!/usr/bin/python
import random
import logging as log

### TODO use list(str) 
log.warning("Started..")
beast = input("Enter the ultimate winner word.\n>> ") # The goal word of the evolution
beast = str(beast).upper().replace(" ", "_")
log.warning("Beast is {}".format(beast))

alphabet = "ABCDEFGHIJKLMNOPRSTUVYZQXW" 
gens = ["_"]
gens.extend([l for l in alphabet]) # Letters that words can have
length = len(beast)
primalword = []

for i in range(length): # Randomly generates Primal Soup
    primalword.append(random.choice(gens))

last_word = "".join(primalword)
generations = [last_word] 
log.warning("Generation list:\n {}".format(generations))

class WordRace: # Word's class
 
    def __init__(self,name="Word") :
        self.name = name
        self.generations = generations
    def mutate(self,old_word): # Changes every %10 of letters randomly
        word = old_word
        for index in range(0,length):
            if random.random() < 0.3 :
                new_gen = random.choice(gens)
                log.warning("old word {}".format(word))
                word_l = list(word)
                log.warning("Word in type of list {}".format(word_l))
                try:
                    word_l[index] = new_gen
                except IndexError:
                    raise IndexError(word_l,index)
                if type(word_l) != None:
                    word = "".join(word_l) 
                else:
                    raise TypeError("type of word_l is None")
                if type(word) == None:
                    raise TypeError
                log.warning("new word {}".format(word))
        return word

    def reproduce(self,elder_word):
        generation = []
        num_of_child = random.randint(2,10)

        for i in range(num_of_child): # Generates new 2 to 10 words and mutates it in %70 posiblity
            if random.random() >= 0.3 :
                if type(elder_word) == list:
                    elder_word  = "".join(elder_word)
                log.warning("Elder word {}".format(elder_word))
                new_word = self.mutate(elder_word)
            else:
                new_word = elder_word
            generation.append(new_word)

        generations.append(generation)
        print("Every generation that has lived:")
        for g in generations:
            print(g)
        
        def selection(generation): # Applies natural selection in accordance to their similarities with beast
            success = []
            for w in generation: # Give a score for similarities with beast for each word
                score = 0
                log.warning("w is{}".format(w))
                assert w != None
                c = 0
                for l in w: # TODO w gives NoneType object 
                    if l == beast[c]:
                        score +=1
                    c += 1
                success.append((w,score))
# [("ads",1), ("dda",9),("nn",9)]
            log.warning("Success rate of words is {}".format(success) )
            scores = []
            for s in success:
                scores.append(s)
            
            for p in success:
                for q in success:
                    if (p[1] == q[1]) and (p != q):
                        to_be_deleted = random.choice((p,q))
                        try:
                            success.remove(to_be_deleted)
                        except ValueError:
                            continue
            log.warning("New success rate of words is {}".format(success))
            scores.sort()
            highest_score = scores[0]
            winner = ""
            for s in success:
                if s[1] == highest_score:
                    winner = s[0]

            return winner

        return selection(generation)

race = WordRace()

while last_word != beast:
    temp_word = race.reproduce(last_word) 
    last_word = temp_word 
    log.warning("Last word :{}".format(last_word))
