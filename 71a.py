#!/usr/bin/env python3
"""
Solution for https://codeforces.com/problemset/problem/71/A
"""

__author__ = "Ryan Harris"
__version__ = "0.1.0"
__license__ = "MIT"
import sys

def main():
    """ Main entry point of the app """
    s = sys.stdin.read()
    splits = s.splitlines()
    del splits[0]
    for i in splits:
        if len(i) > 10:
            print(i[0] + str(len(i)-2) + i[-1])
        else:
            print(i)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main() 