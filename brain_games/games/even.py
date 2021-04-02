"""Game module game even."""
import random


def rule_of_game():
    """Do this outputs rule of even game."""
    print('Answer "yes" if the number is even, otherwise answer "no".')


def game_even():
    """Do this is the number even.

    Returns:
        number: integre random number
        result: string 'yes' or 'no'
    """
    number = random.randint(1, 100)
    result = 'yes' if number % 2 == 0 else 'no'
    return number, result
