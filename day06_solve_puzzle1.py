def parse_map(_map):
	""" Returns a dictionary where from you can look
	up which center a given orbiter has """

	orbits = {}
	for orbit in _map.split("\n"):
		center,  orbiter = orbit.split(")")
		orbits[orbiter] = center

	return orbits

def count_orbits(_map):
	orbits = parse_map(_map)

	orbiters = orbits.keys()
	i = 0
	for obj in orbiters:
		while obj != "COM":
			obj = orbits[obj]
			i += 1
	return i

test_map = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
""".strip("\n \t")

assert count_orbits(test_map) == 42

with open("input06.txt", "r") as f:
	_map = f.read()
	print(count_orbits(_map))