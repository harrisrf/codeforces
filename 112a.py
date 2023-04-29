"""
Solution for https://codeforces.com/problemset/problem/112/A
"""
import sys

def main():
	s = sys.stdin.read()
	lines = s.splitlines()
	first_line = lines[0].lower()
	second_line = lines[1].lower()

	if first_line == second_line:
		print(0)
	elif first_line < second_line:
		print(-1)
	else:
		print(1)

if __name__ == "__main__":
	main()