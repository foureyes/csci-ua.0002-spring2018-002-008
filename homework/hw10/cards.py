"""
cards.py
=====
Create 3 functions that work with playing cards (from a standard 52-card 
deck). For this program, use a dictionary to represent a single card and 
a list of dictionaries to represent a deck of cards or a hand of cards.

Read more about playing cards here:

https://en.wikipedia.org/wiki/Standard_52-card_deck

Each card (dictionary) will have two keys: face and suit.

* the value at the key, 'suit', can be one of the following strings: 
    1. 'hearts'
    2. 'diamonds'
    3. 'clubs'
    4. 'spades'
* the value at the key, 'face', is one of the following strings:
    1. '2' through '10' (all strings)
    2. 'J', 'Q', 'K', 'A'

Create the following functions:

1. make_deck
2. calculate_hand
3. draw

make_deck
-----
Creates a deck of 52 playing cards

* parameters: no parameters
* return: a list of dictionaries
    * each dictionary represents a card (as outlined above)
    * there will be 52 cards
    * each card will be created with a different combination of suite and face
* example:
    deck = make_deck()
    print(deck)
    # prints out ... [{'suit': 'hearts', 'face': '2'}, {'suit': 'hearts', 'face': '3'},   ....
    # and continues through suits and faces
    # {'suit': 'spades', 'face': 'Q'}, {'suit': 'spades', 'face': 'K'}, {'suit': 'spades', 'face': 'A'}]

calculate_hand
-----
Given a set of cards, calculates the numeric value of the set of cards and 
optimizes for a value that is less than or equal to 21. This value is 
calculated by summing the numeric value of each card.

Cards are given the following values:

1. cards with numbers as the face are worth their corresponding numeric value
2. (J)ack, (Q)ueen, and (K)ing are worth 10
3. (A)ces are worth either 1 or 11, which ever brings the total closer to 21 

One algorithm to handle aces is to treat them as 11 by default. Then, if the 
total is greater than 21, for every ace in the set of cards, subtract 10 until
there are no more aces or the total is less than or equal to 21.

* parameters: a list of dictionaries representing a set / hand of cards
* return: an int representing the total numeric value of the set of cards
* example:
    result1 = calculate_hand([
        {'suit': 'hearts', 'face': 'A'}, 
        {'suit': 'diamonds', 'face': 'A'}, 
        {'suit': 'clubs', 'face': 'A'}, 
        {'suit': 'hearts', 'face': '9'}])
    print(result1) # 12

    result2 = calculate_hand([
        {'suit': 'hearts', 'face': 'A'}, 
        {'suit': 'diamonds', 'face': 'A'}, 
        {'suit': 'clubs', 'face': 'A'}, 
        {'suit': 'hearts', 'face': '8'}])
    print(result2) # 21

draw_cards
-----
Retrieve some number of cards randomly from a set / deck of cards

* parameters:
    * a list of dictionaries representing a deck of cards
    * an int representing the number of cards to be drawn
* return: a list of dictionaries representing the cards drawn
* example:
    hand = draw_cards(deck, 3)
    print(hand)
    # [{'suit': 'clubs', 'face': '8'}, {'suit': 'clubs', 'face': 'J'}, {'suit': 'hearts', 'face': '4'}]
"""
