#!/usr/bin/env python3

import re

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

def check_year(year, min, max):
    if len(str(year)) == 4 and int(year) >= min and int(year) <= max:
        return True
    return False

def check_height(height):
    unit_re = re.compile('.*(cm|in)')
    unit = unit_re.match(height)
    if unit and unit.group(1) == 'cm':
        height_re = re.compile('(\d{3})cm')
        height_digits = height_re.match(height)
        if height_digits and int(height_digits.group(1)) >= 150 and int(height_digits.group(1)) <= 193:
            return True
    elif unit and unit.group(1) == 'in':
        height_re = re.compile('(\d{2})in')
        height_digits = height_re.match(height)
        if height_digits and int(height_digits.group(1)) >= 59 and int(height_digits.group(1)) <= 76:
            return True
    return False

def check_haircolor(haircolor):
    haircolor_re = re.compile('#([0-9a-f]{6})')
    haircolor_match = haircolor_re.match(haircolor)
    if haircolor_match:
        return True
    return False

def check_eyecolor(eyecolor):
    valid_colors = ['amb','blu','brn','gry','grn','hzl','oth']
    if eyecolor in valid_colors:
        return True
    return False

def check_id(id):
    if len(str(id)) == 9:
        return True
    return False

def check_passport(passport):
    required_field = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
    missing_keys = []
    for key in required_field:
        if key not in passport:
            if key == 'cid':
                continue
            missing_keys.append(key)

        if key == 'byr' and key not in missing_keys:
            if not check_year(passport['byr'], 1920, 2002):
                missing_keys.append(key)

        if key == 'iyr' and key not in missing_keys:
            if not check_year(passport['iyr'], 2010, 2020):
                missing_keys.append(key)

        if key == 'eyr' and key not in missing_keys:
            if not check_year(passport['eyr'], 2020, 2030):
                missing_keys.append(key)

        if key == 'hgt' and key not in missing_keys:
            if not check_height(passport['hgt']):
                missing_keys.append(key)

        if key == 'hcl' and key not in missing_keys:
            if not check_haircolor(passport['hcl']):
                missing_keys.append(key)

        if key == 'ecl' and key not in missing_keys:
            if not check_eyecolor(passport['ecl']):
                missing_keys.append(key)

        if key == 'pid' and key not in missing_keys:
            if not check_id(passport['pid']):
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