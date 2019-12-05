"""
a few key facts about the password:

- It is a six-digit number.
- The value is within the range given in your puzzle input.
- Two adjacent digits are the same (like 22 in 122345).
- Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).

How many different passwords within the range given in your puzzle input meet these criteria?
"""

def is_ascending(numbers):
	ns = str(numbers)
	return all([ns[i] <= ns[i+1] for i in range(len(ns)-1)])

def has_same_adjacent(numbers):
	ns = str(numbers)
	return any([ns[i] == ns[i+1] for i in range(len(ns)-1)])


def check_rules(password, _min=0, _max=999999, length=6):
	return all((
		len(str(password)) == length,
		password <= _max,
		password >= _min,
		is_ascending(password),
		has_same_adjacent(password)
	))
	 


assert check_rules(111111) == True
assert check_rules(223450) == False
assert check_rules(123789) == False

_MIN = 146810
_MAX = 612564

print("puzzle 1:\t",sum([check_rules(i, _MIN, _MAX) for i in range(_MIN, _MAX+1)]))

def has_lonely_pair(numbers):
	""" A lonely pair is 2 of the same digits not followed by another same digit 
	In this context a pair is one digit followed by the same digit. 
	Fx, [1,1] will have a pair at index 0 and a non-pair at index 1
	"""

	ns = str(numbers)
	# Determine if each digit is followed by the same digit, and thereby is a pair
	has_pair = [ns[i] == ns[i+1] for i in range(len(ns)-1)]
	# We are looking for a pair not followed by another pair
	return any([has_pair[i] and not has_pair[i+1] for i in range(len(has_pair)-1)])

def check_exanded_rules(password, _min=0, _max=999999, length=6):
	return all((
		len(str(password)) == length,
		password <= _max,
		password >= _min,
		is_ascending(password),
		has_lonely_pair(password)
	))

assert check_exanded_rules(112233) == True
assert check_exanded_rules(122333) == True
assert check_exanded_rules(123444) == False
assert check_exanded_rules(111122) == True

print("puzzle 2:\t",sum([check_exanded_rules(i, _MIN, _MAX) for i in range(_MIN, _MAX+1)]))