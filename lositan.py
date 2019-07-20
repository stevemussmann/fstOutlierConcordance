class Lositan():
	'Class for handling Lositan output'

	def __init__(self, f, p):
		self.f = f
		self.bal = 0.0+p
		self.pos = 1.0-p
		self.d = dict()

	def readLositan(self):
		with open(self.f) as lf:
			for line in lf:
				if not line.startswith("Locus\tHet"):
					(locus, het, fst, p) = line.split("\t")
					locus=locus.replace("Locus","")
					self.d[locus] = float(p)
		print(self.d)

	def printSignificant(self):
		fhb = open("lositan.balancing_selection.txt", 'w')
		fhp = open("lositan.positive_selection.txt", 'w')
		for locus,pval in self.d.items():
			if(pval < self.bal):
				print(locus,"\t",pval,"\t","balance")
				fhb.write(locus)
				fhb.write("\n")
			elif(pval > self.pos):
				print(locus,"\t",pval,"\t","positive")
				fhp.write(locus)
				fhp.write("\n")
				
