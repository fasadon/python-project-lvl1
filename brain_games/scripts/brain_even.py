#!/usr/bin/env python3
"""Main program brain even."""


from brain_games.games.even import game_even, rule_of_game
from brain_games.engine import engine


def main():
    """Interface brain-even."""
    engine(game_even, rule_of_game)


if __name__ == '__main__':
    main()
