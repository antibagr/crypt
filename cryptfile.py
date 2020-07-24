from .fileholder import fileholder
from .config import BYTESIZE
from .log import log
from .cryptograph import cryptograph


class SumException(Exception):
	pass

class cryptfile():

	"""
	# cryptfile - encryption class, has two functions
	cf - encrypts file
	df - decrypts file 

	"""

	def filedecorator(f):
		"""
		# Here we use decorator to log start and end time
		# And make sure that file exists and it's not empty
		"""
		def wrapper(filename):
			log.start()
			if fileholder.notempty(filename):
				log.fileinfo("Reading file",filename)
				cryptograph.lines = fileholder.readfile(filename)
				f(filename)
				action = "Encryption" if f.__name__ == 'cf' else "Decryption"
				log.fileinfo(action+" completed",filename)
			else:
				log.message("'{}' is empty".format(filename))
			log.end()
		return wrapper

	@filedecorator
	def cf( filename ):
		"""
		# First we get lines from the file
		# Next we try to check the sum of it. If it's not encrypted
		# Then we shuffle default dictionary random number of times
		# Then we generate secret key
		# Also we encrypt shuffled dictionary and save it to private variable
		# Then line by line we encrypt all file using secret key
		# After all we open file again
		# And replace normal text with encrypted version of it
		# We add the secret key and shuffled dictionary 
		# At the end of the file separeted with pointer
		# Generated in cryptograph class
		"""
		lines = cryptograph.lines
		if not cryptograph.checksum(lines[0]):
			log.message('Start encryption')
			cryptograph.shuffledict()
			key = cryptograph.getkey()
			dictionary = cryptograph.hidedict()
			clines = [ cryptograph.c(x,key) for x in lines]
			with open(filename,'w') as f:
				log.message('Writing encryted text')
				for c in clines:
					f.write(c)
				key = str(key).rjust(BYTESIZE,'0')
				dictionary = dictionary.rjust(BYTESIZE,'0')
				f.write(cryptograph.getkeysign(key))
				f.write(cryptograph.getdictsign(dictionary))

		else:
			log.message("'{}' is already encrypted".format(filename))
			raise SumException(f"{filename} is already encrypted")
	 
	@filedecorator
	def df(filename):
		"""
		First we get single encrypted line from the file
		Next we check the sum of it. If it's really encrypted
		Then we find secret key and shuffled dictionary 
		After it we divide whole line into single bytes and 
		Decrypt then using secret key
		After all we write down pure text into file instead of numbers
		"""
		line = cryptograph.lines
		if cryptograph.checksum(line[0]):
			log.message('Start decryption')
			line,key = cryptograph.parsekey(line)
			bytestring = [ int(line[x:x+BYTESIZE]) for x in range(0,len(line),BYTESIZE)]
			clines = cryptograph.dc(bytestring,key)
			with open(filename,'w') as f:
				log.message('Writing decryted text')
				for l in clines:
					f.write(l)
		else:
			log.message("'{}' is not encrypted".format(filename))
			raise SumException(f"{filename} is not encrypted")
		
	def isencrypted(filename):
		if fileholder.notempty(filename):
			result = cryptograph.checksum(fileholder.readfile(filename)[0])	 
		else:
			result = False
		notword = str() if result else 'not '
		log.message(f"{filename} is {notword}encrypted")
		return result
