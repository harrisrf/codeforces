#!/usr/bin/env python3
"""
Solution for https://codeforces.com/problemset/problem/4/A
"""

__author__ = "Ryan Harris"
__version__ = "0.1.0"
__license__ = "MIT"
def main():
    """ Main entry point of the app """
    s = input()
    w = int(s)
    result = "NO"

    for i in range(4, w+1, 2):
        if (w - i) % 2 == 0:
            result = "YES"
            break

    print(result)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()