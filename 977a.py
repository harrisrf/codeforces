"""
Solution for https://codeforces.com/problemset/problem/977/A
"""

def main():
	s = input()
	row = s.split(" ")
	n = int(row[0])
	k = int(row[1])
	for i in range(k):
		if n % 10 == 0:
			n = n // 10
		else:
			n = n - 1
	print(n)

if __name__ == '__main__':
	main()