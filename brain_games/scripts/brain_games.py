#!/usr/bin/env python3
"""Main program."""


from brain_games.cli import welcome_user


def hello():
    """Hello for user."""
    print('Welcome to the Brain Games!')


def main():
    """Main interface"""
    hello()
    welcome_user()


if __name__ == '__main__':
    main()
