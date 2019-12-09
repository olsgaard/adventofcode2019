from collections import defaultdict

def parse_map(_map):
	""" Returns a dictionary where from you can look
	up which center a given orbiter has """

	orbits = {}
	for orbit in _map.split("\n"):
		center,  orbiter = orbit.split(")")
		orbits[orbiter] = center

	return orbits

def count_orbits(_map, start_obj):
	orbits = parse_map(_map)

	obj = start_obj
	path = {}
	i = 0
	while obj != "COM":
		obj = orbits[obj]
		i += 1
		path[obj] = i

	return path

def find_shortest_connection(_map):
	you = count_orbits(_map, "YOU")
	santa = count_orbits(_map, "SAN")

	for center in santa.keys():
		if you.get(center):
			return santa[center] + you[center] - 2

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
K)YOU
I)SAN
""".strip("\n \t")

assert find_shortest_connection(test_map) == 4

with open("input06.txt", "r") as f:
	_map = f.read()
	print(find_shortest_connection(_map))