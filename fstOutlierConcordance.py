#!/usr/bin/env python3

from comline import ComLine
from bayescan import BayeScan
from lositan import Lositan
from compare import Compare

import sys

def main():
	input = ComLine(sys.argv[1:])

	#handle bayescan output
	bs = BayeScan(input.args.bayescan,input.args.fdr)
	bsCommand = bs.build_command()
	bs.run_program(bsCommand)
	print(input.args.bayescan)

	#handle lositan output
	los = Lositan(input.args.lositan,0.025)
	los.readLositan()
	los.printSignificant()

	#compare outputs
	com = Compare("bayescan.outliers.txt","lositan.positive_selection.txt")
	com.readInput()
	com.printResults()


main()

raise SystemExit
