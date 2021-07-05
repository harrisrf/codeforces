"""
Solution for https://codeforces.com/problemset/problem/266/A
"""

import sys

def main():
	s = sys.stdin.read()
	lines = s.splitlines()
	n = int(lines[0])
	data = lines[1]
	result = 0 
	for i in range(n-1):
		if data[i] == data[i+1]:
			result += 1
	print(result)

if __name__ == '__main__':
	main()