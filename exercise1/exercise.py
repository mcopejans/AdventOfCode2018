from exercise1 import puzzle_input

def parse_input(input):
    split_input = input.split('\n')
    return [int(x) if x.startswith('-') else int(x[1:]) for x in split_input]

def main():
    initial_frequency = 0
    input = puzzle_input.PUZZLE_INPUT
    parsed_input = parse_input(input)

    final_frequency = initial_frequency + sum(parsed_input)
    print("Final frequency part 1: {}".format(final_frequency))

    # Part 2
    reached_frequencies = set()
    reached_frequencies.add(initial_frequency)
    reached_frequency = initial_frequency
    while True:
        for frequency_diff in parsed_input:
            reached_frequency += frequency_diff
            if reached_frequency in reached_frequencies:
                print("Final frequency part 2: {}".format(reached_frequency))
                return 0
            else:
                reached_frequencies.add(reached_frequency)

if __name__ == "__main__":
    main()
