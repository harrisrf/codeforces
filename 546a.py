"""
Solution for https://codeforces.com/problemset/problem/546/A
n * n+1 / 2 
"""
def main():
	s = input()
	row = s.split(" ")
	cost = int(row[0])
	dollars = int(row[1])
	bananas = int(row[2])
	result = cost * ((bananas * (bananas + 1)) // 2) - dollars
	if result < 0:
		print(0)
	else: 
		print(result)

if __name__ == '__main__':
	main()