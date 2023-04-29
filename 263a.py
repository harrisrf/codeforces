"""
Solution for https://codeforces.com/problemset/problem/263/A
"""
import sys

def main():
	s = sys.stdin.read()
	lines = s.splitlines()
	for i in range(5):
		elements = lines[i].split(" ")
		for j in range(5):
			if elements[j] == "1":
				print(abs(i - 2) + abs(j -2))
				return

if __name__ == "__main__":
	main()