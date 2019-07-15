#!/usr/bin/env python3

from comline import ComLine
from bayescan import BayeScan

import sys

def main():
	input = ComLine(sys.argv[1:])
	bs = BayeScan(input.args.bayescan,input.args.fdr)
	bsCommand = bs.build_command()
	bs.run_program(bsCommand)
	print(input.args.bayescan)


main()

raise SystemExit
