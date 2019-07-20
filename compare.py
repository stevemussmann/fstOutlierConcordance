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

	def printResults(self, vcf):
		counter=0
		keep = dict()
		out = vcf + ".select.vcf"
		fho = open(out, 'w')
		for locus, count in self.d.items():
			if count > 1:
				keep[locus]=count
				print(locus)

		with open(vcf) as vcfh:
			for line in vcfh:
				if line.startswith("#"):
					print(line)
					fho.write(line)
				else:
					counter+=1
					if str(counter) in keep:
						print(line)
						fho.write(line)


