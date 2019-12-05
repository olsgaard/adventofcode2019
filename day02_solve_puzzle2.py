"""
An Intcode program is a list of integers separated by commas 
(like 1,0,0,3,99). To run one, start by looking at the first 
integer (called position 0). Here, you will find an opcode - 
either 1, 2, or 99. The opcode indicates what to do; for example, 
99 means that the program is finished and should immediately halt.
Encountering an unknown opcode means something went wrong.

Opcode 1 adds together numbers read from two positions and 
stores the result in a third position. 
The three integers immediately after the opcode tell you these 
three positions - the first two indicate the positions from 
which you should read the input values, and the third indicates 
the position at which the output should be stored.

For example, if your Intcode computer encounters 1,10,20,30, 
it should read the values at positions 10 and 20, add those values, 
and then overwrite the value at position 30 with their sum.

Opcode 2 works exactly like opcode 1, except it multiplies the 
two inputs instead of adding them. Again, the three integers after 
the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by 
stepping forward 4 positions.
"""

def run_intcode(intcode):
	intcode = intcode.copy()
	for i in range(len(intcode)//4):
		i = i*4

		parameter1_address = intcode[i+1] 
		parameter2_address = intcode[i+2]
		output_address = intcode[i+3]

		if intcode[i] == 1:
			intcode[output_address] = intcode[parameter1_address]+intcode[parameter2_address]
		elif intcode[i] == 2:
			intcode[output_address] = intcode[parameter1_address]*intcode[parameter2_address]
		else:
			return intcode

	return intcode

def calculate_output(intcode):
	return run_intcode(intcode)[0]

assert run_intcode([1,0,0,0,99]) == [2,0,0,0,99]
assert run_intcode([2,3,0,3,99]) == [2,3,0,6,99]
assert run_intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert run_intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

## Puzzle 2 code

def pretty_print_intcode(intcode):
	for i in range(4,len(intcode),4): 
		print(i-4,  
		intcode[i-4:i]) 

def set_1202_alarm_state(intcode):
	intcode = intcode.copy()
	intcode[1] = 12
	intcode[2] = 2
	return intcode

def set_alarm(intcode, noun, verb):
	intcode = intcode.copy()
	intcode[1] = noun
	intcode[2] = verb
	return intcode

with open("input02.txt", 'r') as f:
	intcode = [int(i) for i in f.read().split(",")]

pretty_print_intcode(intcode)

#Puzzle 1 solution
print(calculate_output(set_1202_alarm_state(intcode)))

# Puzzle 2 solution
# It finishes in half a second, but it feels very hacky
for i in range(100):
	for j in range(100):
		output = calculate_output(set_alarm(intcode, i, j))
		if output == 19690720:
			print(f"noun={i}, verb={j}, alarm code = {100*i + j}")










