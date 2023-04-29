#!/usr/bin/env python3
"""
Solution for https://codeforces.com/problemset/problem/158/A
"""

__author__ = "Ryan Harris"
__version__ = "0.1.0"
__license__ = "MIT"
import sys

def main():
    s = sys.stdin.read()
    lines = s.splitlines()
    first_line = lines[0].split(" ")
    n = int(first_line[0])
    k = int(first_line[1])
    scores_str = lines[1].split(" ")
    scores_int = [int(i) for i in scores_str]
    scores_int.sort(reverse=True)
    counter = 0
    for i in scores_int:
        if i > 0 and i >= scores_int[k-1]:
            counter += 1
    print(counter)

if __name__ == "__main__":
    main() 