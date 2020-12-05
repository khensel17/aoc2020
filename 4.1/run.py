#!/usr/bin/env python3

def parse_data(file):
    data_file = open(file, 'r')
    data = data_file.read().splitlines()

    passports = []
    attr = {}
    for line_number, line in enumerate(data):
        # print(line)
        key_value = line.split(' ')
        # print(key_value)

        for i in key_value:
            # print(i)
            if '' not in key_value:
                key = i.split(':')[0]
                value = i.split(':')[1]
                # print(key)
                # print(value)
                attr[key] = value
        if ('' in key_value) or (line_number == (len(data) - 1)):
                passports.append(attr)
                attr = {}
                continue
    return passports

def check_passport(passport):
    required_field = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
    missing_keys = []
    for key in required_field:
        if key not in passport:
            if key == 'cid':
                continue
            missing_keys.append(key)
    return missing_keys

def main():
    passports = parse_data('data')

    # print("{}".format(passports))
    # print(len(passports))

    number_valid_passports = 0

    for passport in passports:
        missing = check_passport(passport)
        # print(missing)
        # print(len(missing))
        if len(missing) == 0:
            number_valid_passports += 1
    print("# valid passports: {}".format(number_valid_passports))

if __name__== "__main__":
  main()