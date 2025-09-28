def slice_string(string, start=0, stop=None, step=1):
	"""
		Primary function to slice string
		@param string: The text or list which needs to be sliced
		@param start: Start index
		@param stop: Stop index
		@param step: Step, the number by which the slicing should increment.

		@returns tuple
	"""
	# Variable to hold final output
	result = ""
	string_length = len(string)

	# Raise exception if step = 0
	if step == 0:
		raise ValueError("Step cannot be 0")

	start, stop = set_start_stop(string, start, stop, step)
	
	# Proceed only if string is not empty or None
	if string:
		if start >= 0 and stop is None:
			# If stop index is None then we just return the index value
			result = string[start]
		elif start >= 0:
			# Set the index variable to start index
			index = start
			# If start and stop index is valid then proceed
			if is_valid(start, stop, step):
				# Loop through the string
				for s in string:
					# stop execution if index equals stop index
					if index == stop:
						break
					# Raise exception if index does not exists. 
					# Append the string to result 
					try:
						result += string[index]
					except IndexError:
						pass
					# Increment the index by step. This allows us to skip characters by step.
					index += step

	return result

def set_start_stop(string, start, stop, step):
	"""
		Calculate the start, stop depending on step.
		@param string: The text or list which needs to be sliced
		@param start: Start index
		@param stop: Stop index
		@param step: Step, the number by which the slicing should increment.

		@returns tuple
	"""
	string_length = len(string) 
	if step > 0:
		# If step is a positive number and user has not provided the start and stop index.
		# Then set the start index to 0 and stop index to the string/list length.
		if type(stop) == str:
			stop = string_length
		if type(start) == str:
			start = 0
	else:
		# If step is a negative number and user has not provided the start and stop index.
		# Then set the start index to string/list length - 1 and stop index to 0.
		# We do this for reversing the string.
		if type(stop) == str:
			stop = 0
		if type(start) == str:
			start = string_length - 1

	# If start is negative, then update the start index to be length - start.Similar logic for stop index.
	# This piece of logic handles the negative number input. It converts then into a positive index for the string/list.
	if start < 0:
		start = string_length + start
	if stop is not None:
		if stop < 0:
			stop = len(string) + stop

	# Safe case. If start goes below 0 then set it to 0.
	if start < 0:
		start = 0
	# This is a special case. We are doing this only for one case.
	# When we do string[1::-1], it prints index 1 and 0. So to handle that scenario we are updating the stop index to -1 only when the step is negative and stop index is 0.
	# If this is not done, then our output will only be index 1. index 0 will not be printed.
	if step < 0 and stop == 0:
		stop = -1

	return (start, stop)

def is_valid(start, stop, step):
	"""
		Validate if calculated start and stop are valid.
		@param start: Start index
		@param stop: Stop index
		@param step: Step, the number by which the slicing should increment.
	"""
	valid = False
	if step > 0:
		valid = (stop > start)
	elif step < 0:
		valid = (start > stop)

	return valid
