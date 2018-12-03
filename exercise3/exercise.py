from exercise3 import puzzle_input

import re

import numpy as np

def parse_input(input):
    split_input = input.split('\n')
    return [re.search(r'(\#[0-9]+)\ \@\ ([0-9]+)\,([0-9]+)\:\ ([0-9]+)x([0-9]+)', x).groups() for x in split_input]

def count_differing_characters(word, word2):
    count = 0
    differing_character = ''
    for letter, letter2 in zip(word, word2):
        if letter != letter2:
            if count == 1:
                return 0, ''
            differing_character = letter
            count += 1
    return count, differing_character

def main():
    input = puzzle_input.PUZZLE_INPUT
    parsed_input = parse_input(input)

    fabric = np.zeros((1000, 1000))
    count_overlap = 0
    for claim in parsed_input:
        x1 = int(claim[1])
        y1 = int(claim[2])
        x2 = x1 + int(claim[3])
        y2 = y1 + int(claim[4])
        claimed_fabric = fabric[x1:x2,y1:y2]
        count_overlap += np.sum(claimed_fabric[claimed_fabric == 1])
        claimed_fabric += 1

    print("Overlapped claimed fabric part 1: {}".format(count_overlap))

    intact_fabric = np.where(fabric == 1)
    for claim in parsed_input:
        x1 = int(claim[1])
        y1 = int(claim[2])
        w = int(claim[3])
        h = int(claim[4])
        x2 = x1 + w
        y2 = y1 + h
        if np.sum(fabric[x1:x2,y1:y2]) == w*h:
            print("No overlapping claimed fabric part 2: {}".format(claim[0]))
            return 0
    return -1

if __name__ == "__main__":
    main()
