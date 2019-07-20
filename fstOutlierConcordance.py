#!/usr/bin/env python3

from comline import ComLine
from bayescan import BayeScan
from lositan import Lositan

import sys

def main():
	input = ComLine(sys.argv[1:])
	bs = BayeScan(input.args.bayescan,input.args.fdr)
	bsCommand = bs.build_command()
	bs.run_program(bsCommand)
	print(input.args.bayescan)
	los = Lositan(input.args.lositan,0.025)
	los.readLositan()


main()

raise SystemExit
