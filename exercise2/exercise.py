from exercise2 import puzzle_input

def parse_input(input):
    return input.split('\n')

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

    counter2 = 0
    counter3 = 0
    for word in parsed_input:
        found2 = False
        found3 = False
        for letter in word:
            count = word.count(letter)
            if count == 3 and not found3:
                counter3 += 1
                found3 = True
            elif count == 2 and not found2:
                counter2 += 1
                found2 = True

    print("Checksum part A is: {}".format(counter3 * counter2))

    # Part 2
    for word in parsed_input:
        for word2 in parsed_input:
            count, char = count_differing_characters(word, word2)
            if count == 1:
                index = word.find(char)
                print("Common letters part 2: " + word[0:index] + word[index+1:])
                return 0
    return -1

if __name__ == "__main__":
    main()
