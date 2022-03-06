from card_deck import FrenchDeck
from random import choice

deck_of_cards = FrenchDeck()

# it has become iterable
# for card in deck_of_cards:
#     print(card)

# slicing
print(f'Sliced deck {deck_of_cards[0:9]}')

# reverse the deck
print(f'Reversed deck {deck_of_cards[::-1]}')

# draw a random card


