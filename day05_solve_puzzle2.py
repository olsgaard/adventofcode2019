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

		elif opcode == 5:
			parameter1 = parse_parameter(intcode, i+1, C)
			if parameter1 != 0:
				parameter1 = parse_parameter(intcode, i+2, B)
				i = parameter1
			else:
				i += 3

		elif opcode == 6:
			parameter1 = parse_parameter(intcode, i+1, C)
			if parameter1 == 0:
				parameter2 = parse_parameter(intcode, i+2, B)
				i = parameter2
			else:
				i += 3			

		elif opcode == 7:
			parameter1 = parse_parameter(intcode, i+1, C)
			parameter2 = parse_parameter(intcode, i+2, B)

			to_store = int(parameter1 < parameter2)

			intcode[intcode[i+3]] = to_store

			i += 4

		elif opcode == 8:
			parameter1 = parse_parameter(intcode, i+1, C)
			parameter2 = parse_parameter(intcode, i+2, B)

			to_store = int(parameter1 == parameter2)

			intcode[intcode[i+3]] = to_store

			i += 4

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


large_testcode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

assert execute_intcode(large_testcode, -7)[1] == [999]
assert execute_intcode(large_testcode, 0)[1] == [999]
assert execute_intcode(large_testcode, 7)[1] == [999]
assert execute_intcode(large_testcode, 5)[1] == [999]
assert execute_intcode(large_testcode, -2000)[1] == [999]

assert execute_intcode(large_testcode, 8)[1] == [1000]

assert execute_intcode(large_testcode, 9)[1] == [1001]
assert execute_intcode(large_testcode, 10)[1] == [1001]
assert execute_intcode(large_testcode, 999)[1] == [1001]

with open("input05.txt", 'r') as f:
	intcode = [int(i) for i in f.read().split(",")]

executed_intcode, outputs, final_position = execute_intcode(intcode, 5)
diagnotstic_code = outputs[0]
print(executed_intcode)
assert len(outputs) == 1, print(outputs)
print(diagnotstic_code)