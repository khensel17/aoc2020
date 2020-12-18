#!/usr/bin/env python3

import re

def get_degrees(facing):
    if facing == "N":
        degrees = 0
    elif facing == "E":
        degrees = 90
    elif facing == "S":
        degrees = 180
    elif facing == "W":
        degrees = 270
    return degrees

def get_facing(degrees):
    if degrees > 360:
        degrees -= 360
    elif degrees < 0:
        degrees += 360
    elif degrees == 360:
        degrees = 0
        
    if degrees == 0:
        facing = "N"
    elif degrees == 90:
        facing = "E"
    elif degrees == 180:
        facing = "S"
    elif degrees == 270:
        facing = "W"
    print(facing)
    return facing

def parse_input(file):
    data_file = open(file, 'r')
    data = data_file.read().splitlines()

    output = []

    for line in data:
        re_string = re.compile('([NSEWLRF])([0-9]{1,})')
        re_match = re_string.match(line)
        if re_match:
            instruction = re_match.group(1)
            num = re_match.group(2)
            output.append({'instr': instruction, 'num': int(num)})
    return output

def main():
    # data = parse_input('example')
    data = parse_input('input')

    sum_ab_ns = 0
    sum_ab_ew = 0
    facing = "E"

    print(data)
    for line in data:
        print("####################################")
        degrees = get_degrees(facing)
        if (facing == "E" and line['instr'] == "F") or line['instr'] == "E":
            sum_ab_ew += line['num']
        elif (facing == "W" and line['instr'] == "F") or line['instr'] == "W":
            sum_ab_ew -= line['num']
        elif (facing == "N" and line['instr'] == "F") or line['instr'] == "N":
            sum_ab_ns += line['num']
        elif (facing == "S" and line['instr'] == "F") or line['instr'] == "S":
            sum_ab_ns -= line['num']
        elif line['instr'] == "R":
            degrees += line['num']
            facing = get_facing(degrees)
        elif line['instr'] == "L":
            degrees -= line['num']
            facing = get_facing(degrees)

        print("North-south: {}".format(sum_ab_ns))
        print("East-west: {}".format(sum_ab_ew))

    print("Result {} + {}: {}".format(abs(sum_ab_ew), abs(sum_ab_ns), (abs(sum_ab_ew) + abs(sum_ab_ns))))

if __name__=="__main__":
    main()