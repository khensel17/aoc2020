#! /usr/bin/python
import sys

with open ('input') as f:
    lines = f.read().splitlines()
    for line_org in lines:
        # print(line_org)
        for line_add in lines:
            # print(line_add)
            for line_add2 in lines:
                sum = int(line_org)  + int(line_add) + int(line_add2)
                # print('SUM: {0}'.format(sum))
                if int(sum) == 2020:
                    print('FOUND match: {0} + {1} + {2}'.format(line_org, line_add, line_add2))
                    print('Multiplied: {0}'.format((int(line_org)*int(line_add)*int(line_add2))))
                    sys.exit(0)
