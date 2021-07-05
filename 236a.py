"""
Solution for https://codeforces.com/problemset/problem/236/A
"""

def main():
	s = input()
	set_s = set(s)
	if len(set_s) % 2 == 0:
		print("CHAT WITH HER!")
	else:
		print("IGNORE HIM!")

if __name__ == '__main__':
	main()