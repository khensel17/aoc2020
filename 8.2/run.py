#!/usr/bin/env python3

def parse_input(file):
    data_file = open(file, 'r')
    data = data_file.read().splitlines()

    instructions = []
    for line in data:
        split_line = line.split(' ')
        command = split_line[0]
        argument = split_line[1]
        count_executed = 0
        instruction = {'command':command, 'argument':argument, 'count_executed': count_executed}
        instructions.append(instruction)
    return instructions

def main():
    # instructions = parse_input('example')
    instructions = parse_input('input')
    # print(instructions)

    instruction_index = 0
    accumulator = 0

    while True:
        print("Current index: {}\nAccumulator: {}\nOperation: {}\nArgument: {}\nCount: {}\n\n".format(instruction_index, accumulator, instructions[instruction_index]['command'], instructions[instruction_index]['argument'], instructions[instruction_index]['count_executed']))
        if instructions[instruction_index]['command'] == 'acc':
            accumulator += int(instructions[instruction_index]['argument'])
            instructions[instruction_index]['count_executed'] += 1
            instruction_index += 1
        elif instructions[instruction_index]['command'] == 'jmp':
            instructions[instruction_index]['count_executed'] += 1
            instruction_index += int(instructions[instruction_index]['argument'])
        elif instructions[instruction_index]['command'] == 'nop':
            instructions[instruction_index]['count_executed'] += 1
            instruction_index += 1

        if instruction_index > (len(instructions) - 1) or instructions[instruction_index]['count_executed'] == 1:
            print("Accumulator: {}".format(accumulator))
            return False

if __name__== "__main__":
  main()