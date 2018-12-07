from exercise5 import puzzle_input

import numpy as np


def remove_type(polymer, type):
    polymer_ascii = map(ord, polymer)
    for i in reversed(range(len(polymer))):
        char_ascii = polymer_ascii[i]
        if char_ascii in type:
            del polymer_ascii[i]
    polymer = ''.join(map(chr, polymer_ascii))
    return polymer

def react_polymer(polymer):
    polymer_ascii = map(ord, polymer)
    polymer_ascii_np = np.array(polymer_ascii)
    diff_np = np.ediff1d(polymer_ascii_np)
    indices_reaction_np = np.where(np.logical_or(diff_np == 32, diff_np == -32))[0]

    prev_i = 0
    for i in np.flip(indices_reaction_np):
        if i == prev_i - 1:  # Prevent double deletion in case of e.g. cCc.
            continue
        del polymer_ascii[i + 1]
        del polymer_ascii[i]
        prev_i = i
    polymer = ''.join(map(chr, polymer_ascii))
    return polymer, indices_reaction_np.size

def build_types():
    return [[lower, upper] for lower, upper in zip(range(ord('a'), ord('z')), range(ord('A'), ord('Z')))]

def main():
    polymer = puzzle_input.PUZZLE_INPUT
    can_react = 1
    while can_react:
        polymer, can_react = react_polymer(polymer)

    print("Part1: number of units in polymer {}".format(len(polymer)))

    min_length = len(polymer)
    for type in build_types():
        print("Testing type [{}, {}]".format(chr(type[0]), chr(type[1])))
        polymer = puzzle_input.PUZZLE_INPUT
        polymer = remove_type(polymer, type)
        can_react = 1
        while can_react:
            polymer, can_react = react_polymer(polymer)
        length = len(polymer)
        if length < min_length:
            min_length = length

    print("Part2: number of units in min length polymer {}".format(min_length))
    return 0

if __name__ == "__main__":
    main()
