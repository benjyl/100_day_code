
import random
import numpy as np
import os

def check_play():
    """Checks whether user wants to play a game of blackjack

    Returns:
        bool: True if want to play else False
    """
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
    """Deals 2 cards randomly to dealer and player

    Args:
        cards (list): list of integer card values

    Returns:
        list: returns 2 lists, the player cards and computer cards
    """
    player = random.choices(cards, k=2)
    computer = random.choices(cards, k=2)
    return player, computer

def display_cards(player, computer):
    """prints user cards, their sum and first computer card

    Args:
        player (list): list of player cards
        computer (list): list of computer cards
    """
    print(f"Your cards: {player}, current score: {np.sum(player)}")
    print(f"Computer's first card: {computer[0]}\n")

def final_display(player, computer, win=False):
    """Displays end of game state, whether user wins or loses, showing player and computer final hands

    Args:
        player (list): list of player cards
        computer (list): list of computer cards
        win (bool, optional): state of whether player has won. Defaults to False.
    """
    player_score = np.sum(player)
    comp_score = np.sum(computer)
    print(f"Your final cards: {player}, Final score: {player_score}")
    print(f"Computer's Final hand: {computer}, Computer final score: {comp_score}")
    
    
    if win:
        if player_score > comp_score:
            print("Your score was higher than the computer, you win!\n")
        elif comp_score > 21:
            print(f"You win, Computer bust with score of {comp_score}\n")
    else:
        if player_score > 21:
            print("You are bust, you lost\n")
        elif comp_score > player_score:
            print(f"Computer score of {comp_score} higher than your score of {player_score}\nComputer wins\n")
        else:
            print("It's a draw\n")

def check_score(cards):
    """checks sum of player/computer cards, if > 21, checks for ace (11) and changes its score to 1

    Args:
        cards (list): list of cards

    Returns:
        list: list of cards
        integer: sum of the list
    """
    score= np.sum(cards)
    if score > 21:
        if 11 in cards:
            cards = [1 if i == 11 else i for i in cards]
            score = np.sum(cards)
    return cards, score

def get_card(player, computer, cards):
    """asks player if they want more cards when their score is < 21

    Args:
        player (list): player cards
        computer (list): computer cards
        cards (list): deck

    Returns:
        player(list): player cards
        score(int): player's score
    """
    hit = input('Would you like another card? "y" or "n": ').lower()
    player, score = check_score(player)
    while hit == "y":
            player+=random.choices(cards, k=1)
            player, score = check_score(player)
            if score >21:
                break
            else:
                display_cards(player, computer)
                hit = input('Would you like another card? "y" or "n": ').lower()
    return player, score

def computer_get(computer, cards):
    """Adds card to computer deck if under 17

    Args:
        computer (list): computer cards
        cards (list): deck of cards

    Returns:
        computer(list): computer cards
        comp_score(int): computer score
    """
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
    score = np.sum(player)
    comp_score = np.sum(computer)
    if score == 21 and comp_score <21:
        final_display(player,computer, win=True)
    elif score == 21 and comp_score == 21:
        final_display(player, computer)
    else:    
        display_cards(player, computer)
        player, score = get_card(player, computer, cards)
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