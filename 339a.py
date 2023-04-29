"""
Solution for https://codeforces.com/problemset/problem/339/A
"""

def main():
	s = input()
	split_s = s.split("+")
	split_s.sort()
	print("+".join(str(i) for i in split_s))

if __name__ == "__main__":
	main()