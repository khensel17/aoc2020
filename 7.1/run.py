#!/usr/bin/env python3

import re

class Bag:
    def __init__(self, name, containing = [], max_amount = 1):
        self.name = name
        self.containing = containing
        self.max_amount = max_amount

    def contains(self, name):
        if self.containing != '':
            for bag in self.containing:
                # print(bag.name)
                if bag.name == name:
                    # print(bag.name)
                    return True
        return False

    def get_containing(self):
        return self.containing

def parse_input(file):
    data_file = open(file, 'r')
    data = data_file.read().splitlines()
    bags = []
    for line in data:
        contain = line.split('contain')
        segs = (contain[-1].strip()).split(',')
        # print(contain)
        # print(segs)
        subbags_re = re.compile('(\d{1,})\s(.*)bags?.?')
        subbags = []
        for seg in segs:
            subbag_match = subbags_re.match(seg.strip())
            if subbag_match:
                # print(subbag_match.group(1))
                # print(subbag_match.group(2))
                subbag = Bag((subbag_match.group(2)).strip(), max_amount=subbag_match.group(1))
                # print(subbag_match.group(1))
                subbags.append(subbag)
        strip_bag_re = re.compile('(.*)\sbags?')
        strip_bag_match = strip_bag_re.match(contain[0].strip())
        if strip_bag_match:
            bag = Bag(strip_bag_match.group(1), subbags)
            bags.append(bag)
    return bags


def main():
    # print("Hello")
    # bags = parse_input('example')
    bags = parse_input('data')
    # print(bags)
    available_bags = []

    for bag in bags:
        if bag.contains('shiny gold'):
            available_bags.append(bag.name)
            # print(bag.name)
    for abag in available_bags:
        for bag in bags:
            if bag.contains(abag) and bag.name not in available_bags:
                available_bags.append(bag.name)

    print("Total available bags: {}".format(len(available_bags)))

        # for subbag in bag.containing:
        #     # print(subbag.name)
        #     if subbag.contains('shiny gold'):
        #         available_bags.append(subbag.name)
        #         print(subbag.name)

    # for bag in bags:
    #     for subbag in available_bags:
    #         if bag.contains(subbag):
    #             available_bags.append(bag.name)

    # print(available_bags)

    # t = Bag('red',[Bag('shiny gold')],1)
    # print(t.contains('shiny gold'))

if __name__== "__main__":
    main()