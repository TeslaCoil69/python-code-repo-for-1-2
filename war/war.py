#imports

import random
hand1 = []

####################################################
#variable assignments

class card:

   # Class initializer method creates a new playing card with
   # a desired rank and suit provided through the creation
   # parameters.
   #
   # @param self  This is a default python class argument
   # @param suit  Card suit denoted by char (C,H,D,S)
   # @param rank  Card rank denoted by char (2,3,4,5,6,7,8,9,0,J,Q,K,A)
  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank
    self.card = rank + suit
  # end def __init__
    
   # Method returns the class rank as a character
   # 2,3,4,5,6,7,8,9,0,J,Q,K,A
   #
   # @param  self  This is a default python class argument
   # @return rank  Returns the rank of the card
  def getRank(self):
    return self.rank
  # end def getRank

   # Method returns the class suit as a character
   # C,H,D,S
   #
   # @param  self  This is a default python class argument
   # @return suit  Returns the suit of the card
  def getSuit(self):
    return self.suit
  # end def getSuit
    
   # When print is called on a card this method will return
   # the card as a string representation of its suit and
   # rank. (i.e. 3C,AH,0D,KS)
   #
   # @param  self  This is is a default python class argument
   # @return card  Returns the card as a string
  def __str__(self):
    return self.card
  # end def __str__
  
# end class Card

####################################################
#classes
 # The Deck class is used to represent a deck of playing
 # cards each card has a suit and a rank. The deck is 
 # capable of being shuffled and dealing one card at a
 # time.
class Deck:
  
   # Class initializer method creates a new unshuffled deck
   # of cards with all suits and ranks. This deck does not
   # include jokers.
   #
   # @param self  This is a default python class argument
  def __init__(self):
    self.deck = []     # Actual deck representation
    self.cardsUsed = 0 # Keeps track of the cards dealt
  
    self.suits = ['C','H','D','S']
    self.ranks = ['2','3','4','5','6','7','8','9','0','J','Q','K','A']
  
    for suit in self.suits:
      for rank in self.ranks:
        self.deck.append(card(suit,rank))
  # end def __init__
  
   # Method puts all cards back in the deck and then
   # shuffles the deck.
   #
   # @param self  This is a default python class argument
  def shuffle(self):
    for i in range(len(self.deck)-1, 0, -1): 
      
    # Pick a random index from 0 to i  
        j = random.randint(0, i + 1)  
    
        # Swap arr[i] with the element at random index  
        self.deck[i], self.deck[j] = self.deck[j], self.deck[i]  
      
        # Printing shuffled list  
        print ("The shuffled list is : " +  str(self.deck))
        self.cardsUsed = 0
      #end def shuffle

   # Method returns the number of cards left in the deck
   # that can be dealt.
   #
   # @param  self       This is a default python class argument
   # @return cardsLeft  This is the number of cards left in the deck
  def cardsLeft(self):
    return len(self.deck - self.cardsUsed)
  # end def cardsLeft
    
   # Method deals one card from the deck and marks it in the list
   # of cards dealt. Returns an error if no cards are left in the
   # deck.
   #
   # @param  self     This is a default python class argument
   # @error  noCards  Throws/prints a no cards left error
   # @return card     Returns/deals a card 
  def dealCard(self):
    if self.cardsUsed == len(self.deck):
      print ("Error: There are no cards left in the deck.")
    else:
      self.cardsUsed += 1
      return self.deck[self.cardsUsed - 1]
  # end def dealCard
  
   # Method deals any numbers of cards from the deck and marks it 
   # in the list of cards dealt. Returns an error if no cards are 
   # left in the deck.
   #
   # @param  self     This is a default python class argument
   # @param  num      This is the number of cards to deal
   # @error  noCards  Throws/prints a no cards left error
   # @return card     Returns/deals a card 
  def dealCards(self, num):
    if (self.cardsUsed + num) >= len(self.deck):
      print ("Error: There are not enough cards left in the deck.")
    else:
      deal = []
    
      for i in range(num):
        deal.append(self.deck[self.cardsUsed - 1])
        
      return deal
  # end def dealCards

   # When print is called on a deck this method will return
   # the list of cards in the deck as a string representation
   # of each cards suit and rank.
   #
   # @param  self  This is is a default python class argument
   # @return deck  This returns the entire deck to be printed 
  def __str__(self):
    tmpDeck = "Deck: "
    for c in self.deck:
      tmpDeck += str(c) + " "
    return tmpDeck
  # end def __str__
    
# end class Deck


 # The Card class is used to represent a single playing card
 # from a deck of 52 or 54. The card has a suit and a rank.


deck = Deck() # creates and unshuffled deck of cards
deck.shuffle() # shuffles the deck of cards
hand1.append(deck.dealCard()) # Deals a single card from the deck to a hand
print(list(hand1))
####################################################
#modules

####################################################
#main

####################################################


















