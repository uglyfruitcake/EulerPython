def number_of_ways_across_square(size):
    row1 = [1] * size
    row2 = [0] * size
    row2[0] = 1
    grid = [row2] * size
    grid[0] = row1

    for x in xrange(1, size):
        for y in xrange(1, size):
            grid[x][y] = grid[x - 1][y] + grid[x][y - 1]

    return grid[size - 1][size - 1]
