#!/usr/bin/env python3
import sys

with open ('input') as f:
    lines = f.read().splitlines()
    for line_org in lines:
        # print(line_org)
        for line_add in lines:
            # print(line_add)
            sum = int(line_org)  + int(line_add)
            # print('SUM: {0}'.format(sum))
            if int(sum) == 2020:
                print('FOUND match: {0} + {1}'.format(line_org, line_add))
                print('Multiplied: {0}'.format((int(line_org)*int(line_add))))
                sys.exit(0)
