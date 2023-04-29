#!/usr/bin/env python3
"""
Solution for https://codeforces.com/problemset/problem/50/A
"""

__author__ = "Ryan Harris"
__version__ = "0.1.0"
__license__ = "MIT"

def main():
   s = input()
   m_and_n = s.split(" ")
   m = int(m_and_n[0])
   n = int(m_and_n[1])
   if m * n < 2:
    result = 0
   elif (m * n) % 2 == 0:
    result = m * n // 2
   else:
    result = ((m * n) - 1) // 2
   print(result)

if __name__ == "__main__":
    main() 