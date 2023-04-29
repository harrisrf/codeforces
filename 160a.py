"""
Solution for https://codeforces.com/problemset/problem/160/A
"""

import sys

def main():
	s = sys.stdin.read()
	split_s = s.splitlines()
	coins = split_s.split(' ')
	
	running_total = []
	total = 0
	for i in coins:
		running_total.append(int(i))
		total += int(i)

if __name__ == "__main__":
	main()