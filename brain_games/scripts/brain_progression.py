#!/usr/bin/env python3
"""Main program brain progression."""


from brain_games.engine import engine
from brain_games.games.progression import progression, rule_of_game


def main():
    """Interface brain-progression."""
    engine(progression, rule_of_game)


if __name__ == '__main__':
    main()
