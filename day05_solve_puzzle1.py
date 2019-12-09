"""
The TEST diagnostic program will run on your existing Intcode computer after a few modifications:

First, you'll need to add two new instructions:

Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.
Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.
"""

def parse_opcode(opcode: int):
	opcode = str(opcode).rjust(5, "0")
	A,B,C = [int(i) for i in opcode[:-2]]
	opcode = int(opcode[-2:])

	return A,B,C, opcode

def parse_parameter(intcode, idx, mode=0):
	if mode == 0:
		return intcode[intcode[idx]]
	elif mode == 1:
		return intcode[idx]

def execute_intcode(intcode: list, _input=1):
	intcode = intcode.copy()
	output = []

	i = 0
	A, B, C, opcode = parse_opcode(intcode[i])
	while True:
		if opcode == 1:
			parameter1 = parse_parameter(intcode, i+1, C)
			parameter2 = parse_parameter(intcode, i+2, B)

			intcode[intcode[i+3]] = parameter1 + parameter2

			i += 4
		
		elif opcode == 2:
			parameter1 = parse_parameter(intcode, i+1, C)
			parameter2 = parse_parameter(intcode, i+2, B)

			intcode[intcode[i+3]] = parameter1 * parameter2
			
			i += 4

		elif opcode == 3:
			intcode[intcode[i+1]] = _input
			i += 2

		elif opcode == 4:
			parameter1 = parse_parameter(intcode, i+1, C)
			output.append(parameter1)

			i +=2

		elif opcode == 99:
			return intcode, output, i
		else:
			raise ValueError(f"Opcode {opcode} at position {i} is invalid. Current state of intcode:\n {intcode}")

		A, B, C, opcode = parse_opcode(intcode[i])



# Testcases from audentis, https://www.reddit.com/r/adventofcode/comments/e6ob88/2019_day_5_part_1algorithms_dont_understand/f9s81tm/
assert execute_intcode([1101, 5, 6, 5, 99, 0, 11, 12])[0] == [1101, 5, 6, 5, 99, 11, 11, 12]

assert execute_intcode([1,0,0,0,99])[0] == [2,0,0,0,99]
assert execute_intcode([2,3,0,3,99])[0] == [2,3,0,6,99]
assert execute_intcode([2,4,4,5,99,0])[0] == [2,4,4,5,99,9801]
assert execute_intcode([1,1,1,4,99,5,6,0,99])[0] == [30,1,1,4,2,5,6,0,99]

assert execute_intcode([3,3,4,0,99])[0] == [3,3,4,1,99]

with open("input05.txt", 'r') as f:
	intcode = [int(i) for i in f.read().split(",")]

executed_intcode, outputs, final_position = execute_intcode(intcode)
diagnotstic_code = outputs[-1]
print(executed_intcode)
print(outputs)
print(diagnotstic_code)