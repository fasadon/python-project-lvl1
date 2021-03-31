#!/usr/bin/env python3

from brain_games.games.calc import game_calc
from brain_games.games.even import welcome_user


def hello():
    """Hello for user."""
    print('Welcome to the Brain Games!')
    
    
def main():
    """Interface brain-calc."""
    hello()
    name = welcome_user()
    game_calc(name)


if __name__ == '__main__':
    main()
