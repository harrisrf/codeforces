#!/usr/bin/env python3
"""
Solution for https://codeforces.com/problemset/problem/231/A
"""

__author__ = "Ryan Harris"
__version__ = "0.1.0"
__license__ = "MIT"
import sys

def main():
    s = sys.stdin.read()
    lines = s.splitlines()
    del lines[0]
    counter = 0 
    for line in lines:
        elements = line.split(" ")
        if int(elements[0]) + int(elements[1]) + int(elements[2]) > 1:
            counter += 1
    print(counter)

if __name__ == "__main__":
    main() 