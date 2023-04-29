#!/usr/bin/env python3
import sys

def main():
	x = 0
	s = sys.stdin.read()
	lines = s.splitlines()
	del lines[0]
	for line in lines:
		if "++" in line:
			x += 1
		else:
			x -= 1
	print(x)

if __name__ == "__main__":
	main()