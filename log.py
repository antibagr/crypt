import time
import atexit
import os

from .fileholder import fileholder
from .config import LOGDIR

class log():

	'''
	# Log class. Print both informational messages
	# And errors on the screen
	# Use -l in command line to save all logs in log file
	# Desctination of all logs can be set in config.py
	# Use -q in command line to mute all logs
	'''

	silience = False
	savetofile = False

	def logtofile(dirname=None):
		'''
		# User would like to save all messages into a file
		# We register a save function
		# It will be launch when the program ends
		'''
		log.dirname = dirname if dirname else LOGDIR
		log.savetofile = True
		log.messages = ''
		atexit.register(log.savefile)

	def savefile():
		'''
		# All logs save into directory with the name that set in config.py file
		# It can be changed by preference
		# If directory for logs doesn't exist it'll be created
		# We also log end time when saving log file
		'''
		if not log.silience:
			if not os.path.exists(log.dirname):
				os.mkdir(log.dirname)
			filename = 'log_%s' % time.strftime("%Y%m%d-%H%M%S")+'.txt'
			filepath = os.path.join(log.dirname,filename)
			with open(filepath,'w') as f:
				f.write(log.messages)

	def start():
		'''
		# It only will call once from cryptfile
		# A cryptfile asks log to log start time
		'''
		log.starttime = time.time()
		log.message('start time - %s' % time.strftime("%H:%M:%S"))

	def end():
		'''
		# It only will call once when program ends
		'''
		log.endtime = time.time()
		log.message('end time - %s' % time.strftime("%H:%M:%S"))
		log.message('total - %s ms' % round((log.endtime-log.starttime)*1000))

	def mute():
		'''
		# If it's called no logs will be shown or saved
		'''
		log.silience = True

	def fileinfo(msg,filename):
		'''
		# Log filename, filesize and stated message
		# With help of fileholder
		'''
		log.message("{} '{}' ({})".format(msg,filename,fileholder.getsize(filename)))

	def message(msg):
		'''
		# Log message on the screen if log class is not muted
		# Saved message to log file if logtofile() was called
		'''
		if not log.silience:
			if log.savetofile:
				log.messages += msg + '\n'
			print(msg)