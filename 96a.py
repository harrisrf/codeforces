"""
Solution for https://codeforces.com/problemset/problem/96/A
"""

def main():
	s = input()
	if len(s) < 7:
		return("NO")
	run = 0
	for i in range(1, len(s)):
		if s[i] == s[i-1]:
			run += 1
		else:
			run = 0
		if run == 6:
			return('YES')
	return("NO")

if __name__ == "__main__":
	print(main())