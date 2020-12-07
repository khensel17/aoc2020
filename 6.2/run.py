#!/usr/bin/env python3

def parse_data(file):
    data_file = open(file, 'r')
    data = data_file.read().splitlines()

    groups = []
    group = []
    for index, line in enumerate(data):
        if line != '':
            group.append(list(line))
        if line == '' or index == (len(data) - 1):
            groups.append(group)
            group = []
    return groups

def main():
    # groups = parse_data('example')
    groups = parse_data('data')
    sum = 0

    for group in groups:
        unique_yes = []
        count_answers = {}
        num_same_answers = 0
        for person in group:
            for answer in person:
                if answer not in unique_yes:
                    unique_yes.append(answer)
                    count_answers[answer] = 1
                    continue
                count_answers[answer] += 1
        for yes in unique_yes:
            if count_answers[yes] == len(group):
                num_same_answers += 1
        sum += num_same_answers

    print("Sum of all yes answers: {}".format(sum))

if __name__== "__main__":
    main()