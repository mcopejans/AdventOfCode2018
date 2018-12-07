from exercise4 import puzzle_input

import datetime
import numpy as np
import re

REGEX_EXPRESSION = r'\[([0-9]+)\-([0-9]+)\-([0-9]+)\ ([0-9]+)\:([0-9]+)\]\ ([a-zA-Z\ ]+(\#[0-9]+)?)'

class Guard(object):
    def __init__(self, time, id):
        self._id = id
        self._time = time
        self._items = {}

    def add_item(self, time, value):
        self._items[time] = value

    def count_sleeping_minutes(self):
        sleeping_minutes = 0
        minute_asleep = 0
        minutes = np.zeros((60, 1))
        for key in sorted(self._items.iterkeys()):
            value = self._items[key]
            if value == "falls asleep":
                sleeping_minutes -= key.minute
                minute_asleep = key.minute
            else:
                sleeping_minutes += key.minute
                minutes[minute_asleep:key.minute] += 1
        max = np.max(minutes)
        return sleeping_minutes, max, np.where(minutes == max),

def parse_input(input):
    split_input = input.split('\n')
    # [1518-11-01 00:00] Guard #10 begins shift
    groups = [re.search(REGEX_EXPRESSION, x).groups() for x in split_input]
    groupdict = {}
    for x in groups:
        xtime = datetime.datetime(int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4]), 0)
        groupdict[xtime] = x[5]

    return groupdict


def main():
    input = puzzle_input.PUZZLE_INPUT
    parsed_input = parse_input(input)

    guards = {}
    current_guard = None
    for key in sorted(parsed_input.iterkeys()):
        if parsed_input[key][0:5] == "Guard":
            id = parsed_input[key]
            if id not in guards:
                guards[id] = Guard(key, id)
            current_guard = guards[id]
        else:
            current_guard.add_item(key, parsed_input[key])

    max_sleeping_minutes = 0
    max_index = 0
    guard_max_sleeping_minutes = None
    for key in guards.iterkeys():
        guard = guards[key]
        sleeping_minutes, _, index = guard.count_sleeping_minutes()
        if sleeping_minutes > max_sleeping_minutes:
            max_sleeping_minutes = sleeping_minutes
            max_index = index
            guard_max_sleeping_minutes = guard

    print("Part1: Guard with most sleeping minutes: {}, minute asleep: {}".format(guard_max_sleeping_minutes._id, max_index))

    max_sleeping_minutes = 0
    max_index = 0
    guard_max_sleeping_minutes = None
    for key in guards.iterkeys():
        guard = guards[key]
        sleeping_minutes, max, index = guard.count_sleeping_minutes()
        if max > max_sleeping_minutes:
            max_sleeping_minutes = max
            max_index = index
            guard_max_sleeping_minutes = guard
    print("Part1: Guard with most sleeping minutes: {}, minute asleep: {}".format(guard_max_sleeping_minutes._id, max_index))
    return -1

if __name__ == "__main__":
    main()
