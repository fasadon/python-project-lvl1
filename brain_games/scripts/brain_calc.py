#!/usr/bin/env python3

from brain_games.games.calc import game_calc, rule_of_game
from brain_games.engine import engine
    
    
def main():
    """Interface brain-calc."""
    engine(game_calc, rule_of_game)


if __name__ == '__main__':
    main()
