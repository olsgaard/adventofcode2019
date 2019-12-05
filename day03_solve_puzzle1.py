"""
To fix the circuit, you need to find the intersection point closest to the central port.

All wires begin at origin (0,0), and their path is described as would be on a treasure map:
- `R8` means eight steps to the right
- `U4` means 4 step up
- D for down, and L for left

"""

def convert_path_to_coordinates(wire_path):
	coordinates = []
	current_position = [0,0]

	for instruction in wire_path:
		direction, steps = instruction[0], instruction[1:]
		for i in range(int(steps)):
			if direction == "R":
				current_position[0] += 1
			if direction == "L":
				current_position[0] -= 1
			if direction == "U":
				current_position[1] += 1
			if direction == "D":
				current_position[1] -= 1
			coordinates.append(tuple(current_position))
	return coordinates

def manhatten_distance(coordinates):
	x = coordinates[0]
	y = coordinates[1]

	return abs(x) + abs(y)

def find_distance_closest_cross(first_wire, second_wire):
	first_grid = convert_path_to_coordinates(first_wire)
	second_grid = convert_path_to_coordinates(second_wire)

	intersections = set(first_grid) & set(second_grid)
	distances = [manhatten_distance(coord) for coord in intersections]

	return sorted(distances)[0]

assert find_distance_closest_cross(
	["R8", "U5", "L5", "D3"],
	["U7", "R6", "D4", "L4"]
	) == 6

assert find_distance_closest_cross(
	["R75","D30","R83","U83","L12","D49","R71","U7","L72"],
	["U62","R66","U55","R34","D71","R55","D58","R83"]
	) == 159

assert find_distance_closest_cross(
	["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],
	["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]
	) == 135

with open("input03.txt") as f:
	raw1, raw2 = f.readlines()
	first_wire = raw1.strip().split(",")
	second_wire = raw2.strip().split(",")

print(find_distance_closest_cross(first_wire, second_wire))