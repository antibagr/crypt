'''
# Globally seen variables
# LOGDIR is a name of folder
# Where all logs will be saved
# BYTESIZE affects only the size of encrypted file
# It doesn't affect the encrytion algorythm
'''
import os
LOGDIR = os.path.join(os.path.dirname(__file__),'logs')

BYTESIZE = 3

assert 512 > BYTESIZE > 2, "BYTESIZE can't be less than 2 and more than 1024"