def largest_sum_route_in_triangle(triangle):
    size = len(triangle)

    for x in xrange(size - 1, -1, -1):
        for y in xrange(0, x):
            numbers = [triangle[x][y], triangle[x][y + 1]]
            triangle[x - 1][y] += max(numbers)
    return triangle[0][0]
