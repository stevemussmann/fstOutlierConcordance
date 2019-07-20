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
		parser.add_argument("-l", "--lositan",
							dest='lositan',
							required=True,
							help="Specify a lositan summary file for input."
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
		parser.add_argument("-p", "--pthreshold",
							dest="pthreshold",
							type=float,
							default=0.025,
							help="Specify threshold for parsing lositan output."
		)
		parser.add_argument("-v", "--vcf",
							dest='vcf',
							required=True,
							help="Specify a vcf file for input."
		)
		self.args = parser.parse_args()

		#check if files exist
		self.exists( self.args.bayescan )
		self.exists( self.args.lositan )
		self.exists( self.args.vcf )



	def exists(self, filename):
		if( os.path.isfile(filename) != True ):
			print(filename, "does not exist")
			print("Exiting program...")
			print("")
			raise SystemExit
