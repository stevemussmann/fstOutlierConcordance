#!/usr/bin/env python3

from comline import ComLine

import sys

def main():
	input = ComLine(sys.argv[1:])
	print(input.args.bayescan)


main()

raise SystemExit
