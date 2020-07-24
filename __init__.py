import sys

from .cryptfile import SumException
from .cryptograph import CryptographyException

from .log import log
from .cryptfile import cryptfile
from .cmdview import choosevalue

DEBUG = False

def debug():
	global DEBUG
	DEBUG = True

mute = log.mute
savelogs = log.logtofile

def exceptionwrap(f):
	result = None
	def wrapper(*args):
		nonlocal result
		if not DEBUG:
			try:
				log.message("Start cryptograph (safe mode)")
				result = f(*args)
			except FileNotFoundError as e:
				log.message(e.args[0])
			except KeyboardInterrupt:
				e = '\nProgram stopped by user'
				log.message(e)

			except SumException as e:
				log.message(e)

			except CryptographyException as e:
				log.message('cryptography algorithm raised an exception')
				log.message(e)

			except:
				log.message('Unexpected error:' + str(sys.exc_info()[1]))
			finally:
				log.message('Exit')
				return result
		else:
			return f(*args)

	return wrapper

@exceptionwrap
def encrypt(filename):
	cryptfile.cf(filename)

@exceptionwrap
def isencrypted(filename):
	return cryptfile.isencrypted(filename)

@exceptionwrap
def decrypt(filename):
	cryptfile.df(filename)

@exceptionwrap
def terminal():
	"""
	Controller of the cryptography program with command line interface
	"""
	q = "Choose what to do : (1) encrypt, (2) decrypt "
	operation = choosevalue(q,('1','2'))
	q = "choose a file using absolute or relative path\n"
	filename = choosevalue(q,novalidation=True)
	if operation == '1':
		cryptfile.cf(filename)
	else:
		cryptfile.df(filename)


if __name__=='__main__':
	if len(sys.argv) > 1:
		if '-q' in sys.argv:
			log.mute()
		if '-l' in sys.argv:
			log.logtofile()
	terminal()