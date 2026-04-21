from os import remove
import random
from ssl import socket_error

def deal_card():
    """Returns a random card from a deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def calculated_score(cards):

    """Takes a list of cards and return the score calculated from cards """

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare (u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has a BlackJack"
    elif u_score == 0:
        return "Win with a BlackJack"
    elif u_score > 21:
        return "You went over you lose"
    elif c_score > 21:
        return "Opponent went over, you Win"
    elif u_score > c_score:
        return "You Win"
    else:
        return "You Lose"
    
    
def play_game():       
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False

    for _ in range(2):
        computer_cards.append(deal_card())
        user_cards.append(deal_card())

    while not is_game_over:
        user_score = calculated_score(user_cards)
        computer_score = calculated_score(computer_cards)
        print(f"your cards: {user_cards}, current score {user_score}")
        print(f"computer first card: {computer_cards[0]}")

        if user_score == 0 or computer_score ==0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type'y' to get another card or type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score > 17:
        computer_cards.append(deal_card())
        computer_score = calculated_score(computer_cards)

    print(f"your final hands:{user_cards} and final score:{user_score}")
    print(f"Computer final hands:{computer_cards} and  computer final score:{computer_score}")

    print(compare(user_score, computer_score))


while input("Do you want to play a BlackJack type 'y' or 'n' to end") == "y":
    play_game()