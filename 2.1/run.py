#!/usr/bin/env python3

import sys, re

count_valid_policies = 0

with open('password_policies.txt') as f:
    lines = f.read().splitlines()
    for line in lines:
        print(line)
        string_match_re = re.compile('(\d{1,})-(\d{1,}) (\w): (.*)$')
        matching = string_match_re.match(line)

        min_oc = int(matching.group(1))
        max_oc = int(matching.group(2))
        char = matching.group(3)
        password = matching.group(4)

        # print(min_oc)
        # print(max_oc)
        # print(char)
        # print(password)

        # print('(['+char+']{'+ min_oc +','+ max_oc +'})')
        # policy_re = re.compile('(['+char+']{'+ min_oc +','+ max_oc +'})')
        check_password = re.findall(char,password)

        if check_password:
            if len(check_password) >= min_oc and len(check_password) <= max_oc:
                print('Valid password: {0} - with check {1} {2}-{3}'.format(password,char,min_oc,max_oc))
                count_valid_policies += 1

    print('Total valid passwords: {0}'.format(count_valid_policies))