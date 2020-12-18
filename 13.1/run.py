#!/usr/bin/env python3

def parse_input(file):
    data_file = open(file, 'r')
    data = data_file.read().splitlines()

    busses = data[1].replace('x,', '').split(',')
    output = {}
    output['arrival'] = int(data[0])
    output['busses'] = busses

    return output

def main():
    # data = parse_input('example')
    data = parse_input('input')
    print(data)
    counter = 1
    options = []
    for bus in data['busses']:
        print(bus)
        print(data['arrival'] / int(bus))
        bus_time = int(bus) * (data['arrival'] // int(bus) + 1)
        options.append(bus_time)

    waiting_time = abs(data['arrival'] - min(options))
    bus_id = int(data['busses'][options.index(min(options))])
    print("earliest bus: {}".format(min(options)))
    print("bus id: {}, waiting time: {}, result {}".format(bus_id, waiting_time, (bus_id * waiting_time)))

if __name__=="__main__":
    main()