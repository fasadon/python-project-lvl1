#!/usr/bin/env python3
"""Main program brain prime."""
from brain_games.engine import engine
from brain_games.games.prime import prime, rule_of_game


def main():
    """Interface brain-prime."""
    engine(prime, rule_of_game)


if __name__ == '__main':
    main()
