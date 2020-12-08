#!/usr/bin/env python3

import re

class Bag:
    def __init__(self, name, containing = [], count = 1):
        self.name = name
        self.containing = containing
        self.count = count

    def get_sub_bags(self):
        bags = []
        if self.containing != '':
            for bag in self.containing:
                for i in range(int(bag.count)):
                    bags.append(bag.name)
        return bags

    def contains(self, name):
        if self.containing != '':
            for bag in self.containing:
                if bag.name == name:
                    return True
        return False


def parse_input(file):
    data_file = open(file, 'r')
    data = data_file.read().splitlines()
    bags = []
    for line in data:
        contain = line.split('contain')
        segs = (contain[-1].strip()).split(',')
        subbags_re = re.compile('(\d{1,})\s(.*)bags?.?')
        subbags = []
        for seg in segs:
            subbag_match = subbags_re.match(seg.strip())
            if subbag_match:
                subbag = Bag((subbag_match.group(2)).strip(), count=subbag_match.group(1))
                subbags.append(subbag)
        strip_bag_re = re.compile('(.*)\sbags?')
        strip_bag_match = strip_bag_re.match(contain[0].strip())
        if strip_bag_match:
            bag = Bag(strip_bag_match.group(1), subbags)
            bags.append(bag)
    return bags


def main():
    bags = parse_input('data')
    available_bags = []

    for bag in bags:
        if bag.name == 'shiny gold':
            available_bags.extend(bag.get_sub_bags())
    for i in available_bags:
        for bag2 in bags:
            if bag2.name == i:
                available_bags.extend(bag2.get_sub_bags())

    print("Total number bags: {}".format(len(available_bags)))

if __name__== "__main__":
    main()