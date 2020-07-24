import string
import random

from .config import BYTESIZE

DICT = [x for x in string.printable]

MAXKEY = pow(10,BYTESIZE)-len(DICT)
MAXVALUE = pow(10,BYTESIZE)-1
DICTSIGN = str(MAXKEY*len(DICT)+(MAXVALUE*BYTESIZE))
KEYSIGN = str(MAXVALUE*len(DICT)+(MAXKEY*BYTESIZE))

class cryptograph():

	dictionary = DICT

	def getkey():
		if MAXKEY <= 0:
			raise CryptographyException('There is not enough bytes to crypt. Please, check config file')
		return random.randint(1,MAXKEY)

	def getkeysign(key):
		return KEYSIGN+key

	def getdictsign(dct):
		return DICTSIGN+dct

	def shuffledict():

		cryptograph._d = cryptograph.dictionary[:]
		for i in range(1,random.randint(3,10)):
			random.shuffle(cryptograph._d)

	def c(string,key):
		bytestring = ''
		for symbol in string:
			if symbol in cryptograph.dictionary:
				byte = cryptograph.dictionary.index(symbol)
				byte += key
				if byte > MAXVALUE:
					raise CryptographyException('Out of byte')
				byte = str(byte)
				byte = byte.rjust(BYTESIZE,'0')
				bytestring += str(byte)
			else:
				raise CryptographyException('No such symbol')
		return bytestring
		
	def dc(_bytearray,key):
		string = ''
		for byte in _bytearray:
			string += cryptograph.dictionary[byte-key]
		return string

	def parsekey(line):
		
		if KEYSIGN in line[0]:
			text, _ = line[0].split(KEYSIGN)
			cryptograph._d = _.strip(DICTSIGN)
			key = _[:BYTESIZE]
			return text,int(key)

	def hidedict():
		hiddendict = ''
		for l in cryptograph._d:
			i = str(cryptograph.dictionary.index(l))
			hiddendict += i.rjust(BYTESIZE,'0')
		return hiddendict	

	def checksum(line):
		if KEYSIGN in line:
			a_dict = line.split(DICTSIGN)
			if a_dict[0] == line:
				raise CryptographyException('Bytesize error. Please check if a file was encrypted with current bytesize')
			if len(a_dict[1]) == len(cryptograph.dictionary)*BYTESIZE:
				return True
		return False

class CryptographyException(Exception):
	pass