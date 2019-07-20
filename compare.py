class Compare():
	'Class for comparing Lositan and Bayescan results'

	def __init__(self, b, l):
		self.b = b
		self.l = l
		self.d = dict()

	def readFiles(self,f):
		with open(f) as fh:
			for line in fh:
				locus = line.rstrip()
				if not locus in self.d:
					self.d[locus]=1
				else:
					self.d[locus]+=1

	def readInput(self):
		self.readFiles(self.b)
		self.readFiles(self.l)
		print(self.d)

	def printResults(self):
		for locus, count in self.d.items():
			if count > 1:
				print(locus)

