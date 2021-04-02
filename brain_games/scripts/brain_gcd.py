#!/usr/bin/env python3
"""Main program brain gcd."""
from brain_games.engine import engine
from brain_games.games.gcd import game_gcd, rule_of_game


def main():
    """Interface brain-gcd."""
    engine(game_gcd, rule_of_game)


if __name__ == '__main__':
    main()
