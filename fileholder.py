import os

class fileholder():

	"""
	# fileholder checks if file exist
	# And that file is not empty
	# Also fileholder reads file
	# And has function that returns file's size in readable manner
	"""

	def readfile(filename):
		"""
		# Simply read file with no other actions
		"""
		with open( filename,'r') as f:
			return f.readlines()
	
	def notempty(filename):
		"""
		# Returns false if file is not empty
		# Else True
		"""
		fileholder.checkfilepath(filename)
		if os.path.getsize(filename) == 0:
			return False
		else:
			return True

	def getsize(filename):
		return str(round(os.path.getsize(filename) / 1024,3)) + ' Kb'


	def checkfilepath(filename):
		"""
		# Raise AttributeError both if file doesn't exist
		# Or file has invalid name 
		"""

		p = os.path
		if not os.path.exists(filename):
			raise FileNotFoundError("File '{}' does not exist".format(filename))	
		if os.path.isdir(filename):
			raise FileNotFoundError("'{}' is a directory".format(filename))