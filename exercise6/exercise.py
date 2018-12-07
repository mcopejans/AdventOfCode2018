from exercise6 import puzzle_input

import numpy as np

def parse_input(input):
    split_input = input.split('\n')
    return [map(int, x.split(", ")) for x in split_input]

def find_closest_coord(x, y, coords):
    closest_distance = 1e1000
    closest_coord_index = -1
    distances = []
    for index, coord in enumerate(coords):
        distance = abs(x - coord[0]) + abs(y - coord[1])
        distances.append(distance)
        if distance < closest_distance:
            closest_distance = distance
            closest_coord_index = index

    if distances.count(closest_distance) > 1:
        return -2

    return closest_coord_index

def calculate_total_distance(x, y, coords):
    total_distance = 0
    for index, coord in enumerate(coords):
        distance = abs(x - coord[0]) + abs(y - coord[1])
        total_distance += distance

    return total_distance

def main():
    input = puzzle_input.PUZZLE_INPUT
    coords = parse_input(input)

    # Place coordinates on grid.
    # Initialize grid with -1: not visited
    #                      -2: visited more than once
    max = np.array(coords).max(0)
    grid = -1 * np.ones([max[0] + 1, max[1] + 1])
    for i, coord in enumerate(coords):
        grid[coord[0], coord[1]] = i

    # Find closest coordinate for each point on grid.
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if [x, y] in coords:
                continue
            closest_coord_index = find_closest_coord(x, y, coords)
            grid[x, y] = closest_coord_index

    # Determine infinite coordinate areas.
    infinite_areas = set()
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if x == 0 or x == grid.shape[0] - 1 or y == 0 or y == grid.shape[1] - 1:
                infinite_areas.add(grid[x, y])

    # Determine largest, not infinite area.
    largest_area_size = 0
    for i, coord in enumerate(coords):
        if i not in infinite_areas:
            area_size = grid[grid == i].size
            if area_size > largest_area_size:
                largest_area_size = area_size

    print("Largest area size part 1: {}".format(largest_area_size))

    # Part 2
    grid2 = -1 * np.ones([max[0] + 1, max[1] + 1])
    for i, coord in enumerate(coords):
        grid2[coord[0], coord[1]] = -1

    for x in range(grid2.shape[0]):
        for y in range(grid2.shape[1]):
            total_distance = calculate_total_distance(x, y, coords)
            if total_distance < 10000:
                grid2[x, y] = 1

    size = grid2[grid2 > 0].size
    print("Area total distance points smaller than 10000 part 2: {}".format(size))


if __name__ == "__main__":
    main()
