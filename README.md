@@@ DISCLAIMER @@@

Encryption app. It's built only in educational purpose to demonstrate app maintaining skills.
Do not use it to really hide some information - it's not safe.

Usage:

	Run from your command line:
		python3 __init__.py [-k]
	With optional keys:
		-q Keep quiet, no logging
		-l Logs all message in a log file
		
	Or in your script:
	
		import crypt

		# Use to encrypt file
		crypt.encrypt(filename)
		
		# Use to decrypt file
		crypt.decrypt(filename)

		# additional options

			# Turn on all exceptions
			crypt.debug()
			# Mute all log information
			crypt.mute()
			# Log all information into file
			crypt.savelogs()

	Also you may wanna look up a config.py
