#koty butler hayden whitney christian roberts Dean Church
import pydealer

import time as ti
import random as rd
import tools
#from pydealer.utils import compare_stacks
# Construct a Deck instance, with 52 cards.
deck = pydealer.Deck()
print("deck made")
deck.shuffle()
print("shuffled")
#create and shuffle first deck set
play1 = pydealer.Stack()
play2 = pydealer.Stack()
comp1 = pydealer.Stack()
comp2 = pydealer.Stack()
#create comparison stacks and primary hand stack objects, notice these are acutally holding objects themselves and are not actual stacks

hold = pydealer.Stack()
#party discourse and draw off pile, used to buffer out cards as needed
play1 = deck.deal(26)
play2 = deck.deal(26)
#deal 26 cards to each player hand
data_comp = 0
#used to buffer state data
def retrace():
    global data_comp
    data_comp = rd.random
    deck2 = pydealer.Deck()
    #picks random deck start point and begins comparison of secondary data
    print("deck made")
    deck2.shuffle()
    print("shuffled")
    play12 = pydealer.Stack()
    play22 = pydealer.Stack()
    comp12 = pydealer.Stack()
    comp22 = pydealer.Stack()
    hold2 = pydealer.Stack()
#buffer hold states for transfer initialized and stored here
    play12 = deck.deal(26)
    play22 = deck.deal(26)
    #end buffer operations and return cards that were not compared to each hand
    return data_comp       
result1 = 1
#game state, used to break loops
print(play1)
result = play1 is play2
print(result)
win_state=3
#prints your hand and locks into the loop until done
def test():
    result1 = retrace() #play1 == play2
    global result
    result = True

    
    comp1 = play1.deal(1)
    comp2 = play2.deal(1)
    
    #result = comp1 >= comp2
    reb = retrace()#compare_stacks(comp1, comp2)
    #print(result)
    if reb >= .5:
        print("player1 wins!")
        win_state = 1
    else:
        print("player2 wins!")
        win_state = 2
        

while win_state !=1 and win_state != 2:
    test()
    print("loop finished")
    ti.sleep(.2)
print("winner is player",win_state)

