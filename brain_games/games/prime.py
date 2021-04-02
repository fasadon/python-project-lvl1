"""Game module prime game."""
import random

from brain_games.games.gcd import primfacs


def rule_of_game():
    """Do this outputs rule of prime game."""
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def prime():
    """Do this is the number prime.

    Returns:
        number: random integre number
        string: 'yes' or 'no'
    """
    number = random.randint(1, 100)
    if len(primfacs(number)) == 1:
        return number, 'yes'
    return number, 'no'
