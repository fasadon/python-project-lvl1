#!/usr/bin/env python3
"""Main program brain even."""


from brain_games.even import game_even, welcome_user


def hello():
    """Hello for user."""
    print('Welcome to the Brain Games!')


def main():
    """Interface brain-even."""
    hello()
    name = welcome_user()
    game_even(name)


if __name__ == '__main__':
    main()
