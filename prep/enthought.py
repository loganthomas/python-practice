"""
You are working in a fish factory in the QC automation department.
There isa device that periodically takes pictures of fish
as they move along a conveyor belt.

Your coworker has created an algorithm that converts the pictures
from the conveyor belt to a binary-valued M x N matrix where
"1" indicates "fish" and "0" indicates "not fish" at a given pixel.

Furthermore, your coworker is confident that their algorithm's output
is such that each contiguous region of "1"s represents a single fish.

For example, both of the following would represent a picture with two fish:

[[1, 0, 1, 0],
 [0, 0, 1, 1]]

[[1, 0],
 [0, 1]]

Create a function that accepts a binary image from your coworker's fish
detection algorithm and counts the number of fish contained within it.

[[1, 0, 1, 0],
 [0, 0, 1, 1],
 [1, 0, 1, 0],
 [0, 0, 1, 1],
 [1, 0, 1, 0],
 [0, 0, 1, 1]]
"""

from collections import deque


def search_neighbors(start, image):
    """
    start is tuple (i,j) of location in image matrix
    """
    nrows, ncols = len(image), len(image[0])

    # double ended queue so that acts as FIFO (queue)
    need_to_search = deque([start])

    row, col = start

    # Mark as visited
    image[row][col] = 0

    # Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while need_to_search:
        # grab and remove first comers (not what was just appended)
        i, j = need_to_search.popleft()

        for di, dj in directions:
            ni, nj = i + di, j + dj

            # if location is valid (within boundaries of matrix)
            # and the location has a fish (i.e. == 1), then
            # append to queue and mark as visited
            if (0 <= ni < nrows) and (0 <= nj < ncols) and image[ni][nj] == 1:
                image[ni][nj] = 0  # Mark as visited
                need_to_search.append((ni, nj))
    return image


def count_fish(image):
    if not image or not image[0]:
        return 0

    nrows, ncols = len(image), len(image[0])
    fish_count = 0
    for i in range(nrows):
        for j in range(ncols):
            if image[i][j] == 1:  # Found a new fish
                fish_count += 1
                # Explore and mark the entire fish
                # (i.e look for neighboring pixels)
                image = search_neighbors((i, j), image)

    return fish_count


if __name__ == '__main__':
    print('Problem 1:')
    image = [
        [1, 0, 1, 0],
        [0, 0, 1, 1],
    ]
    print('\n'.join([str(row) for row in image]))
    print(f'fish: {count_fish(image)}')
    print()

    print('Problem 2:')
    image = [
        [1, 0],
        [0, 1],
    ]
    print('\n'.join([str(row) for row in image]))
    print(f'fish: {count_fish(image)}')
    print()

    print('Problem 3:')
    image = [
        [1, 0, 1, 0],
        [0, 0, 1, 1],
        [1, 0, 1, 0],
        [0, 0, 1, 1],
        [1, 0, 1, 0],
        [0, 0, 1, 1],
    ]
    print('\n'.join([str(row) for row in image]))
    print(f'fish: {count_fish(image)}')
