#!/usr/bin/env python3

import re, math

def parse_data(file):
    data_file = open(file, 'r')
    data = data_file.read().splitlines()

    boardpasses = []
    for line in data:
        row = []
        col = []

        line_re = re.compile('([FB]{7})([LR]{3})')
        line_match = line_re.match(line)

        if line_match:
            row_str = line_match.group(1)
            col_str = line_match.group(2)
            for c in list(row_str):
                row.append(c)
            for c in list(col_str):
                col.append(c)
            boardpass = {'row': row, 'col': col}
            boardpasses.append(boardpass)
    return boardpasses

def det_row(start, end, dir):
    # print("start: {} end: {}".format(start, end))
    half = round(((end + 1) - (start + 1)) / 2)
    # print(half)
    if dir == 'F':
        if half == 0:
            return -1, start
        else:
            return (start), (end - half)
    elif dir == 'B':
        if half == 0:
            return -1, end
        else:
            return (start + half), (end)
    elif dir == 'L':
        if half == 0:
            return -1, start
        else:
            return (start), (end - half)
    elif dir == 'R':
        if half == 0:
            return -1, end
        else:
            return (start + half), (end)
def main():
    boardpasses = parse_data('data')
    # print(boardpasses)
    seat_ids = []
    for boardpass in boardpasses:
        start_row = 0
        end_row = 127
        start_col = 0
        end_col = 7
        res_row = 0
        res_col = 0
        for dir in boardpass['row']:
            res = det_row(start_row, end_row, dir)
            start_row = res[0]
            end_row = res[1]
            # print(res)
            if res[0] == -1:
                res_row = res[1]
        for dir in boardpass['col']:
            res = det_row(start_col, end_col, dir)
            start_col = res[0]
            end_col = res[1]
            # print(res)
            if res[0] == -1:
                res_col = res[1]
        seat_id = (res_row * 8) + res_col
        seat_ids.append(seat_id)
        # print(seat_id)
    seat_ids.sort()
    # print(seat_ids)
    for index, id in enumerate(seat_ids):
        if (index + 1) <= (len(seat_ids) - 1) and seat_ids[(index + 1)] != (id + 1):
            print("Missing ID: {}".format((id + 1)))


if __name__== "__main__":
    main()