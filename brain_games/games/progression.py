"""Game module progression game."""
import random


def rule_of_game():
    """Do this outputs rule of progression game."""
    print('What number is missing in the progression?')


def progression():
    """Do this generate progression.

    Returns:
        lst_progression: string of progression
        result: string hidden element
    """
    start = random.randint(1, 100)
    step = random.randint(1, 10)
    len_progression = random.randint(5, 10)
    end = (start + (len_progression - 1) * step) + step
    lst_progression = [i for i in range(start, end, step)]
    position = random.randint(0, len(lst_progression) - 1)
    result = str(lst_progression[position])
    lst_progression[position] = '..'
    lst_progression = ' '.join(map(str, lst_progression))
    return lst_progression, result
