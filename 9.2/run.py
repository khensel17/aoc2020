#!/usr/bin/env python3

preamble_len = 25

def parse_input(file):
    data_file = open(file, 'r')
    data = data_file.read().splitlines()
    output = []

    for line in data:
        output.append(line)

    return output

def testMatchPreamble(data, start, index):
    # print(data[start:(start + preamble_len)])
    sum = int(data[index])
    for index_org, org in enumerate(data[start:(start + preamble_len)]):
        for index_add, add in enumerate(data[start:(start + preamble_len)]):
            sum_test = int(org) + int(add)
            if sum == sum_test and index_org != index_add:
                # print("Success: {}: {} - {}".format(sum, org, add))
                return True
    return False

def findSumRange(data, number):
    numbers = []
    for index1, num1 in enumerate(data):
        sum = int(num1)
        numbers.append(int(num1))
        for num2 in data[(index1 + 1):-1]:
            sum += int(num2)
            numbers.append(int(num2))
            if sum == int(number):
                return numbers
            elif sum > int(number):
                numbers = []
                break


def main():
    # data = parse_input('example')
    data = parse_input('input')

    start = 0
    test_index = 25
    while True:
        test = testMatchPreamble(data, start, test_index)
        # print("{}".format(test))
        if test:
            start += 1
            test_index += 1
        else:
            print("No match found for: {}".format(data[test_index]))
            result = findSumRange(data, data[test_index])
            print("Find range sum for {}: {}".format(data[test_index], result))
            print("Result: {}".format((min(result) + max(result))))
            return False


if __name__== "__main__":
  main()