def choosevalue(question,allowedvalues=(),novalidation=False):

	"""
	# Input validation function

	# Parameters:
		question (str) - string that will be displayed to user
		allowedvalues (sequence) - any sequence that contains strings of valid answer
		novalidation (bool) - turns off any validation

	# Returns:

		answer (str) - valid answer if it's in the allowedvalues
		if novalidation is set, returns any answer that is not empty string

	"""

	if isinstance(allowedvalues,bool):
		novalidation = True

	if not hasattr(type(allowedvalues),'__iter__'):
		allowedvalues = (allowedvalues,)
	while True:

		answer = input(str(question))
		if novalidation:
			if answer != '':
				return answer				
		else:
			if answer not in allowedvalues:
				print("your choice '%s' doesn't seem to be in my answer list" % answer)
				continue
			else:
				return answer
