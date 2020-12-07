#!/usr/bin/env python3

def parse_data(file):
    data_file = open(file, 'r')
    data = data_file.read().splitlines()

    groups = []
    group = []
    for index, line in enumerate(data):
        # print(list(line))
        for char in list(line):
            group.append(char)
        if line == '' or index == (len(data) - 1):
            # print(set(group))
            groups.append(list(set(group)))
            group = []
    return groups

def main():
    # groups = parse_data('example')
    groups = parse_data('data')
    # print(groups)

    sum = 0
    for group in groups:
        sum += len(group)

    print("Sum of all yes answers: {}".format(sum))

if __name__== "__main__":
    main()