"""
Solution for https://codeforces.com/problemset/problem/791/A
"""

def main():
	s = input()
	row = s.split(" ")
	a = int(row[0])
	b = int(row[1])
	result = 0
	while a <= b:
		result += 1
		a = a * 3
		b = b * 2
	print(result)

if __name__ == '__main__':
	main()