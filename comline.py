import argparse
import os.path

class ComLine():
	'Class for implementing command line options'
	

	def __init__(self, args):
		parser = argparse.ArgumentParser()
		parser.add_argument("-b", "--bayescan",
							dest='bayescan',
							required=True,
							help="Specify a bayescan fst.txt file for input."
		)
		parser.add_argument("-o", "--out",
							dest='out',
							default="output.txt",
							help="Specify an output file name."
		)
		parser.add_argument("-r", "--fdr",
							dest="fdr",
							type=float,
							default=0.05,
							help="Specify the fdr for bayescan summary."
		)
		self.args = parser.parse_args()

		#check if files exist
		self.exists( self.args.bayescan )



	def exists(self, filename):
		if( os.path.isfile(filename) != True ):
			print(filename, "does not exist")
			print("Exiting program...")
			print("")
			raise SystemExit
