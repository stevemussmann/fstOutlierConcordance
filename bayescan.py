import sys
import subprocess

class BayeScan():
	'Class for handling BayeScan output'

	def __init__(self, f, fdr):
		self.f = f
		self.fdr = fdr

	def run_program(self,string):
		print(string)
		try:
			fn = self.f + ".stdout" #make file name for stdout
			process = subprocess.Popen(string, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			output, err = process.communicate()

			fstdout = open(fn, 'wb')
			fstdout.write(output)
			fstdout.close()
			print(err)
			if process.returncode !=0:
				print("Non-zero exit status:")
				print(process.returncode)
				raise SystemExit
		except(KeyboardInterrupt, SystemExit):
			raise
		except:
			print("Unexpected error:")
			print(sys.exc_info())
			raise SystemExit

	def build_command(self):
		string="./plot_R.r -f " + self.f + " -r " + str(self.fdr)
		return string
