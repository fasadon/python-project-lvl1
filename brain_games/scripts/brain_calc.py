#!/usr/bin/env python3
"""Main program brain calc."""
from brain_games.engine import engine
from brain_games.games.calc import game_calc, rule_of_game


def main():
    """Interface brain-calc."""
    engine(game_calc, rule_of_game)


if __name__ == '__main__':
    main()
