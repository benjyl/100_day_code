############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
import random
import numpy as np
import os


def check_play():
    while True:
        play = input('Play a new game? Click "y" or "n": ').lower()
        if play == "y":
            return True
            break
        elif play == "n":
            return False
            break
        else:
            print("Wrong input, try again")


def deal_cards(cards):
    player = random.choices(cards, k=2)
    computer = random.choices(cards, k=2)
    return player, computer


def display_cards(player, computer):
    print(f"Your cards: {player}, current score: {np.sum(player)}")
    print(f"Computer's first card: {computer[0]}\n")


def final_display(player, computer, win=False):
    player_score = np.sum(player)
    comp_score = np.sum(computer)
    print(f"Your final cards: {player}, Final score: {player_score}")
    print(f"Computer's Final hand: {computer}, Computer final score: {comp_score}")

    if win:
        if player_score > comp_score:
            print("Your score was higher than the computer, you win!\n")
        elif comp_score > 21:
            print(f"You win, Computer bust with score of {comp_score}")
    else:
        if player_score > 21:
            print("You are bust, you lost\n")
        elif comp_score > player_score:
            print(
                f"Computer score of {comp_score} higher than your score of {player_score}\nComputer wins\n"
            )
        else:
            print("It's a draw\n")


def check_score(cards):
    score = np.sum(cards)
    if score > 21:
        if 11 in cards:
            cards = [1 if i == 11 else i for i in cards]
            score = np.sum(cards)
    return cards, score


def get_card(player, computer, cards):
    hit = input('Would you like another card? "y" or "n": ').lower()
    player, score = check_score(player)
    while hit == "y":
        player += random.choices(cards, k=1)
        player, score = check_score(player)
        if score > 21:
            break
        else:
            display_cards(player, computer)
            hit = input('Would you like another card? "y" or "n": ').lower()
    return player, computer, score


def computer_get(computer, cards):
    comp_score = np.sum(computer)
    while comp_score < 17:
        computer += random.choices(cards, k=1)
        comp_score = np.sum(computer)
    return computer, comp_score


play = check_play()

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
while play:
    os.system("cls")
    player, computer = deal_cards(cards)
    if np.sum(player) == 21:
        final_display(player, computer, win=True)
    else:
        display_cards(player, computer)
        player, computer, score = get_card(player, computer, cards)
        if score > 21:
            final_display(player, computer)
        else:
            computer, comp_score = computer_get(computer, cards)
            if comp_score > 21:
                final_display(player, computer, win=True)
            elif score > comp_score:
                final_display(player, computer, win=True)
            else:
                final_display(player, computer)
    play = check_play()

print("End of session, goodbye")
