def is_ascending(number):
	ns = str(number)
	return all([ns[i] >= ns[i-1] for i in range(1, len(ns))])

assert is_ascending(123456) == True
assert is_ascending(1234444456) == True
assert is_ascending(1234566666) == True
assert is_ascending(1111234566666) == True

assert is_ascending(1234566566) == False
assert is_ascending(112211) == False

def has_lonely_pair(number):
	ns = "x" + str(number) + "x"
	lonely_pairs = []
	for i in range(1,len(ns)-2):
		lonely_pairs.append((ns[i-1] != ns[i]) and (ns[i] == ns[i+1]) and (ns[i+1] != ns[i+2]))
	return any(lonely_pairs)

assert has_lonely_pair(112233) == True
assert has_lonely_pair(132213) == True
assert has_lonely_pair(111233) == True
assert has_lonely_pair(123433) == True

assert has_lonely_pair(111234) == False
assert has_lonely_pair(111222) == False
assert has_lonely_pair(123444) == False

def check_exanded_rules(password):
	return is_ascending(password) and has_lonely_pair(password)

def count_valid_passwords(_min, _max):
	""" The min/max values ensures that the length and the range is within the 
	password definition, and there is no need to check for it explicitly """
	
	return sum([check_exanded_rules(password) for password in range(_min, _max+1)])


# Asserts from problem description
assert check_exanded_rules(112233) == True
assert check_exanded_rules(123444) == False
assert check_exanded_rules(111122) == True

assert check_exanded_rules(223450) == False
assert check_exanded_rules(123789) == False

# These are asserts are "hand calculated"
assert check_exanded_rules(111123) == False
assert check_exanded_rules(122333) == True
assert check_exanded_rules(111111) == False
assert check_exanded_rules(123788) == True
assert check_exanded_rules(889999) == True
assert check_exanded_rules(112345) == True
assert check_exanded_rules(122345) == True
assert check_exanded_rules(112311) == False
assert check_exanded_rules(111111) == False
assert check_exanded_rules(123456) == False

print(count_valid_passwords(146810, 612564))