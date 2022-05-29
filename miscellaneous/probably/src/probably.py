#!/usr/bin/env python3

import string
import random
import pyfiglet
from pathlib import Path
import os


def open_file(filename):
    '''
    open a file by name and return the first line
    '''
    with open(filename, 'r') as f:
        return f.readline().strip()


def random_string(s):
    '''
    randomly changes characters in the string
    returns the new string
    '''
    new_string = ''
    for char in s:
        if random.random() < 0.25:
            new_string += char
        else:
            new_string += random.choice(string.ascii_lowercase +
                                        string.digits+"_")
    return new_string


def main():
    flag = open_file(os.path.join(os.path.abspath(
        os.path.dirname(__file__)), 'flag.txt'))
    print(pyfiglet.figlet_format(random_string(flag)))


if __name__ == "__main__":
    main()
