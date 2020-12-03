#!/usr/bin/env python3

import sys, re

count_valid_policies = 0

with open('password_policies.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        print(line)
        string_match_re = re.compile('(\d{1,})-(\d{1,}) (\w): (.*)$')
        matching = string_match_re.match(line)

        first_pos_char = int(matching.group(1))
        second_pos_char = int(matching.group(2))
        char = matching.group(3)
        password = matching.group(4)

        matched = 0
        for index, character in enumerate(password):
            if index == (first_pos_char - 1) and character == char:
                print('Match: {0} - with char {1} on pos {2}'.format(password,char,first_pos_char))
                matched += 1
            elif index == (second_pos_char - 1) and character == char:
                print('Match: {0} - with char {1} on pos {2}'.format(password,char,second_pos_char))
                matched += 1

        if matched == 1:
            print('Valid password: {0}'.format(password))
            count_valid_policies += 1

    print('Total valid passwords: {0}'.format(count_valid_policies))