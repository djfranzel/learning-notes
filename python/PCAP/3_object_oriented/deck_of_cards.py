import random

class Deck:
    def __init__(self) -> None:
        self.cards = []
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.cards = [Card(suit, value) for suit in suits for value in values]
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0: 
            return self.cards.pop() # pop returns the last element and deletes it, cool!
        else:
            return None
    
    def count_remaining(self):
        return len(self.cards)
    
    def get_remaining(self):
        return [card.present() for card in self.cards]

class Card:
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value
    
    def present(self):
        return self.value + ' of ' + self.suit
    

new_deck = Deck()
new_deck.shuffle()
new_deck.deal()
new_deck.deal()
new_deck.deal()
print(new_deck.get_remaining())
print(new_deck.count_remaining())

# this will do most basic card operations on the deck
