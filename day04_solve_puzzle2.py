assert check_exanded_rules(112233) == True
assert check_exanded_rules(123444) == False
assert check_exanded_rules(111122) == True

assert check_exanded_rules(111123) == False
assert check_exanded_rules(122333) == True
assert check_exanded_rules(111111) == False
assert check_exanded_rules(223450) == False
assert check_exanded_rules(123789) == False
assert check_exanded_rules(123788) == True
assert check_exanded_rules(889999) == True
assert check_exanded_rules(112345) == True
assert check_exanded_rules(122345) == True
assert check_exanded_rules(112311) == False
assert check_exanded_rules(111111) == False
assert check_exanded_rules(123456) == False