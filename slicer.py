def slice_string(string, start=0, stop=None, step=1):
	result = ""
	string_length = len(string)

	if step == 0:
		raise ValueError("Step cannot be 0")

	start, stop = set_start_stop(string, start, stop, step)
	
	if string:
		if start >= 0 and stop is None:
			result = string[start]
		elif start >= 0:
			index = start
			if is_valid(start, stop, step):
				for s in string:
					print(index, stop)
					if index == stop:
						break
					try:
						result += string[index]
					except IndexError:
						pass
					
					index += step

	return result

def set_start_stop(string, start, stop, step):
	string_length = len(string)
	if step > 0:
		if type(stop) == str:
			stop = string_length
		if type(start) == str:
			start = 0
	else:
		if type(stop) == str:
			stop = 0
		if type(start) == str:
			start = string_length - 1

	if start < 0:
		start = string_length + start
	if stop is not None:
		if stop < 0:
			stop = len(string) + stop

	if start < 0:
		start = 0
	if step < 0 and stop == 0:
		stop = -1

	return (start, stop)

def is_valid(start, stop, step):
	valid = False
	if step > 0:
		valid = (stop > start)
	elif step < 0:
		valid = (start > stop)

	return valid
