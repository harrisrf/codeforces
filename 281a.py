"""
Solution for https://codeforces.com/problemset/problem/281/A
"""
def main():
	s = input()
	capital_letter = s[0].upper()
	result = capital_letter + s[1:]
	print(result)

if __name__ == "__main__":
	main()