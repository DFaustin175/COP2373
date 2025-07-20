import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.fullName = f"{rank} of {suit}"

    def __str__(self):
        return self.fullName

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.cardList = []
        for suit in suits:
            for i, rank in enumerate(ranks):
                self.cardList.append(Card(rank, suit))
        self.hand = []
        self.discardPile = []
        random.shuffle(self.cardList)
        self.current_card = 0

    def deal(self):
        for i in range(5):
            newCard = self.cardList.pop()
            self.hand.append(newCard)

    def draw(self, cardIndex):
                newCard = self.cardList.pop()
                self.discardPile.append(self.hand[cardIndex])
                self.hand[cardIndex] = newCard

    def newHand(self):
        self.discardPile.append(self.hand)
        self.hand.clear()
        for i in range(5):
            newCard = self.cardList.pop()
            self.hand.append(newCard)

    def refresh(self):
        self.cardList.append(self.discardPile)
        self.cardList.append(self.hand)
        self.hand.clear()
        self.discardPile.clear()
        random.shuffle(self.cardList)

def main():
    print("Welcome to poker.")
    deck = Deck()

    print("Dealing cards...\n")
    deck.deal()

    print("Your hand:")
    for card in deck.hand:
        print(card.fullName)
    print("\n")

    answer = input("Replace cards?: ")
    while answer.lower() == 'y' or answer.lower() == 'yes':
        drawCards(deck)
        answer = input("Replace more cards?: ")

    print("\nFinal hand:")
    for card in deck.hand:
        print(card.fullName)


def drawCards(deck):
    cardIndex = int(input("Which card would you like to replace?: "))
    print("Replacing cards...")
    deck.draw(cardIndex - 1)
    for card in deck.hand:
        print(card.fullName)

main()

