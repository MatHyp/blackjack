import random
# from replit import clear
from art import *


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_score = 0
computer_score = 0

player_cards = []
computer_cards = []

playAgain = 'y'
# play = input("Do you want play a game of Blackjack? Type 'y' or 'n'")


for num in range(random.randint(1, 4)):
    choice = random.choice(cards)
    computer_cards.append(choice)
    computer_score = computer_score + choice


for num in range(2):
    choice = random.choice(cards)
    player_cards.append(choice)
    player_score = player_score + choice

print(logo)

print(f"    Your cards are: {player_cards} , current score {player_score}")
print(f"    Computer first card: {computer_cards[0]}")

while playAgain == 'y':
    playAgain = input('Type "y" to get other card, type"n" to pass:')

    if playAgain == 'y':
        choice = random.choice(cards)
        player_cards.append(choice)
        player_score = player_score + choice

    if player_score > 21:
        print(f'You went over {player_score}')
        print(computer_score)
        break

print(player_score)
print(computer_score)
