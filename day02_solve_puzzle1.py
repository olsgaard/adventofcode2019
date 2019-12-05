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
	for i in range(len(intcode)//4):
		i = i*4

		input_pos1 = intcode[i+1] 
		input_pos2 = intcode[i+2]
		output_pos = intcode[i+3]

		if intcode[i] == 1:
			intcode[output_pos] = intcode[input_pos1]+intcode[input_pos2]
		elif intcode[i] == 2:
			intcode[output_pos] = intcode[input_pos1]*intcode[input_pos2]
		else:
			return intcode

	return intcode


assert run_intcode([1,0,0,0,99]) == [2,0,0,0,99]
assert run_intcode([2,3,0,3,99]) == [2,3,0,6,99]
assert run_intcode([2,4,4,5,99,0]) == [2,4,4,5,99,9801]
assert run_intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

def set_1202_alarm_state(intcode):
	intcode[1] = 12
	intcode[2] = 2
	return intcode

with open("input02.txt", 'r') as f:
	intcode = set_1202_alarm_state([int(i) for i in f.read().split(",")])

print(run_intcode(intcode)[0])











