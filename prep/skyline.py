"""
The Skyline Problem
-------------------
A city's skyline is the outer contour of the silhouette formed by all
the buildings in that city when viewed from a distance.

Suppose you are given the locations and height of all the buildings in
a cityscape. Write a program to output the skyline formed by these
buildings.

The geometric information of each building is represented by a triplet
of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the
left and right edge of the ith building and Hi is its height.

The output is a list of "key points" in the format [[x1, y1], ...].
A key point is the left endpoint of a horizontal line segment.
Note that the last key point, where the rightmost building ends,
is merely used to mark the termination of the skyline, and always has
zero height.

Also, the ground between any two adjacent buildings should be considered
part of the skyline contour.

https://yao.page/posts/the-skyline-problem-python/

Example:
----------
Input: [
    [2, 9, 10], [5, 12, 12], [3, 7, 15],
    [19, 24, 8], [15, 20, 10]
]

Output: [
    [2, 10], [3, 15], [7, 12], [12, 0],
    [15, 10], [20, 8], [24, 0]
]
"""

# Notes based on observations
# - A point can only be a key point if its y-coord differs from the
#   preceding key point
# - Every key point seems to be located at the edge of the building.
#   Not every building edge is a key point, but when we do find a key
#   point, it happens to be a building's edge


# 1. Determine the existence of key points at specific x-coordinates
#    (i.e. at the buildings edges)
# 2. Keep track of preceding key points we've identified
# 3. Keep track of the candidate buildings for each examined
#    x-coordinate

# Step 1
# Re-organize the input data.
# Segment buildings by x-coord and placing them into sub-segments
# depending on whether left or right side falls on a give x value
#
# The result of this is our sorted scan dict (returned as scan list):
#     [(2, defaultdict(list, {'left': [0]})),
#      (3, defaultdict(list, {'left': [2]})),
#      (5, defaultdict(list, {'left': [1]})),
#      (7, defaultdict(list, {'right': [2]})),
#      (9, defaultdict(list, {'right': [0]})),
#      (12, defaultdict(list, {'right': [1]})),
#      (15, defaultdict(list, {'left': [4]})),
#      (19, defaultdict(list, {'left': [3]})),
#      (20, defaultdict(list, {'right': [4]})),
#      (24, defaultdict(list, {'right': [3]}))]

# Step 2 and 3
# At this point, we don't know all the candidate buildings for each
# x-coord. We need to determine this as we traverse down the scan list
# - Use a heap (called active) to keep track of the candidate buildings
# - We are primarily concerned with with tallest building but the heap
#   used in Python is a "min heap". heap[0] is the smallest item!
#   The interesting property of a heap is that a[0] is ALWAYS its
#   smallest element.
# - We can ensure the tallest buildings are stored at the top of the
#   heap by negating the building heights (For example, -15 and -10 will
#   result in -15 building stored as heap[0] where 15 and 10 would have
#   stored 10 building as heap[0]).
#
# - For every x-coord we scan, if we find that there are "incoming"
#   buildings (i.e. their left edge falls on x), we'll add those
#   buildings to the heap.
# - Similarly, we'll pop buildings whose right edges we've crossed out
#   of the heap, because these buildings are no longer relevant to our
#   key point analysis
#
# The result of this process is shown in detail below:
#
# Iteration 0
# x: 2
# data: defaultdict(<class 'list'>, {'left': [0]})
# adding incoming...
# start active: []
# end active: [Active(val=-10, b=Building(l=2, r=9, h=10))]
# case 1
# start res: []
# end res: [(2, 10)]
# Here, we have our fist building edge (x=2 and it's a left edge of
# building 0). Since active is empty, we don't pop
# anything from the heap. We push this data onto the heap since it is a
# left edge. Be sure to notice that we are negating the building height.
# Since res is empty, `not res` will return True, and we append our
# first key point to the result list (i.e. res). Notice that we use x
# and active[0].b.h since active[0] is building 0 and has a height of 10


# Iteration 1
# x: 3
# data: defaultdict(<class 'list'>, {'left': [2]})
# adding incoming...
# start active: [Active(val=-10, b=Building(l=2, r=9, h=10))]
# end active: [Active(val=-15, b=Building(l=3, r=7, h=15)),
#              Active(val=-10, b=Building(l=2, r=9, h=10))]
# case 3
# start res: [(2, 10)]
# end res: [(2, 10), (3, 15)]
# Here, we have our second x-coord, 3, that belongs to building 2 and is
# it's left edge. Since active[0] is building 0 (which has a `r` of 9)
# and since x is now 3, we don't pop anything from the heap (9 is not
# <= 3). We push this data onto the heap since it is a left edge. Now,
# res is non-empty so case 1 is ignored. active (our heap) is also non-
# empty so we ignore case 2. active[0] is now building 2 since -15 is
# less than -10 and our heap is a min-heap object. Thus, active[0].b.h
# is 15 and res[-1][1] is 10. Since 15 != 10, we conduct case 3 and
# append a new keypoint to the result list (i.e. res). Similar to
# case 1, we use the current x-coord (3) and active[0].b.h (15) as the
# height

# Iteration 2
# x: 5
# data: defaultdict(<class 'list'>, {'left': [1]})
# adding incoming...
# start active: [Active(val=-15, b=Building(l=3, r=7, h=15)),
#                Active(val=-10, b=Building(l=2, r=9, h=10))]
# end active: [Active(val=-15, b=Building(l=3, r=7, h=15)),
#              Active(val=-10, b=Building(l=2, r=9, h=10)),
#              Active(val=-12, b=Building(l=5, r=12, h=12))]
# Here, we have our third x-coord, 5, that belongs to building 1 and is
# it's left edge. Since active[0] is now building 2 (which has a `r` of
# 7) and since x is now 5, we don't pop anything from the heap (7 is not
# <= 5). We push this data onto the heap since it is a left edge. Both
# case 1 and case 2 are skipped as res and active are non-empty.
# Remember that active[0] is now building 2. Thus, active[0].b.h is 15
# and res[-1][1] is also 15 (see previous iteration). Therefore, case 3
# is also skipped.

# Iteration 3
# x: 7
# data: defaultdict(<class 'list'>, {'right': [2]})
# removing candidates...
# start active: [Active(val=-15, b=Building(l=3, r=7, h=15)),
#                Active(val=-10, b=Building(l=2, r=9, h=10)),
#                Active(val=-12, b=Building(l=5, r=12, h=12))]
# end active: [Active(val=-12, b=Building(l=5, r=12, h=12)),
#              Active(val=-10, b=Building(l=2, r=9, h=10))]
# case 3
# start res: [(2, 10), (3, 15)]
# end res: [(2, 10), (3, 15), (7, 12)]
# Here, we have the next x-coord, 7, that belongs to building 2 and is
# it's RIGHT edge. Since active[0] is building 2 (which has a `r` of 7)
# and since x is now 7, (7 <= 7), we can now pop from the heap. Since
# building 2 is located at active[0] this will removed building 2 from
# the heap. This makes intuitive sense because we have now "exhausted"
# building 2 and no longer need to consider it for the remaining
# processes. After removing candidates, we can see that building 1 is
# now located at active[0].
# Notice that since this is a RIGHT edge, we also do not push to the
# heap.
# Case 1 and case 2 are skipped as both res
# and active are non-empty. Now, active[0] is building 1 with a height
# of 12 and res[-1][1] is 15. Since 12 != 15, we append a key point to
# res at (7, 12) corresponding to (x, active[0].b.h).

# Iteration 4
# x: 9
# data: defaultdict(<class 'list'>, {'right': [0]})
# Here, we have the next x-coord, 9, that belongs to building 0 and is
# it's RIGHT edge. Since active[0] is now building 1 (which has `r` of
# 12) and since x is now 9, (12 is not <=9) so we don't pop anything
# from the heap. We also do not add any incoming to the heap since this
# is a right edge of building 0. Case 1 and Case 2 are skipped as both
# res and active are non-empty. Since active[0] is building 1 with a
# height of 12 and since res[-1][1] is also 12 (see previous iteration)
# case 3 is skipped as well. We do nothing in this iteration.

# Iteration 5
# x: 12
# data: defaultdict(<class 'list'>, {'right': [1]})
# removing candidates...
# start active: [Active(val=-12, b=Building(l=5, r=12, h=12)),
#                Active(val=-10, b=Building(l=2, r=9, h=10))]
# end active: [Active(val=-10, b=Building(l=2, r=9, h=10))]
# removing candidates...
# start active: [Active(val=-10, b=Building(l=2, r=9, h=10))]
# end active: []
# case 2
# start res: [(2, 10), (3, 15), (7, 12)]
# end res: [(2, 10), (3, 15), (7, 12), (12, 0)]
# Here, we have the next x-coord, 12, that belongs to building 1 and is
# it's right edge. Since active[0] is currently building 1 (which has
# a `r` of 12) and since x is now 12, (12 <=12), so we pop from the heap.
# The resulting heap now has building 0 as active[0].
# Notice that this is a while loop! active is still non-empty and our
# current x is 12. The resulting heap now has building 0 as active[0]
# which has a `r` of 9. Our x is 12 and our active[0].b.r is 9 and since
# 9 <= 12, we remove all candidates from the heap. This intuitively
# makes because we have reached the end of building 1 (when x is 12) and
# the previous iteration did nothing. Thus, we have "exhausted" building
# 1 and building 0. We can see that the result is an empty heap. Since
# active is now empty, not active will return True, and case 2 is
# executed. Notice that we append (12,0) corresponding to (x,0) because
# we have exhausted all candidates and it is the "end" of this chunk of
# the skyline.

# Iteration 6
# x: 15
# data: defaultdict(<class 'list'>, {'left': [4]})
# adding incoming...
# start active: []
# end active: [Active(val=-10, b=Building(l=15, r=20, h=10))]
# case 3
# start res: [(2, 10), (3, 15), (7, 12), (12, 0)]
# end res: [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10)]
# Here, we begin a new chunk of the skyline with the next x-coord 15
# that belongs to building 4 and is its left edge. Since active is
# empty, we don't pop from the heap. We add this data to the heap and
# active[0] is now building 4. Since res and active are now non-empty,
# case 1 and case 2 are skipped. Our heap has active[0] as building 4
# with a height of 10. Since res[-1][1] is 0, and 10 != 0, we append
# a key point to res as (15, 10) which is (x, active[0].b.h.)

# Iteration 7
# x: 19
# data: defaultdict(<class 'list'>, {'left': [3]})
# adding incoming...
# start active: [Active(val=-10, b=Building(l=15, r=20, h=10))]
# end active: [Active(val=-10, b=Building(l=15, r=20, h=10)),
#              Active(val=-8, b=Building(l=19, r=24, h=8))]
# Here, we have our next x-coord, 19 that belongs to building 3 and is
# its left edge. Since active[0] is building 4 with a `r` of 20 and
# since x is now 19, 20 is not <= 19 so we don't pop from the heap.
# We add this data to the heap since it is a left edge. Notice that
# since building 3 has a height of 8, active[0] still remains as
# building 4 (the smallest element when considering the heap; the
# largest building height between these two buildings since we negated
# the heights). Since res and active are both non-empty, case 1 and
# case 2 are skipped. Now, active[0] is still building 4 with a height
# of 10. res[-1][1] is 10 (see previous iteration). Since these are
# equal, case 3 is skipped. We only pushed to the heap in this iteration.

# Iteration 8
# x: 20
# data: defaultdict(<class 'list'>, {'right': [4]})
# removing candidates...
# start active: [Active(val=-10, b=Building(l=15, r=20, h=10)),
#                Active(val=-8, b=Building(l=19, r=24, h=8))]
# end active: [Active(val=-8, b=Building(l=19, r=24, h=8))]
# case 3
# start res: [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10)]
# end res: [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8)]
# Here, we have the next x-coord, 20, which belongs to building 4 and is
# its right edge. Since active[0] is building 4 with `r` = 20 and since
# x is currently 20, we remove candidates from the heap (pop). This will
# remove building 4 from the heap and makes sense since we have now
# exhausted building 4. The resulting heap will now have building 3 as
# active[0].
# Notice that since this is a right edge, we don't push to the heap.
# Since res and active are both non-empty, we skip case 1 and
# case 2. Now that active[0] is building 3, active[0].b.h is now 8.
# Since res[-1][1] is 10, we add a key point to res as (20, 8) which
# is (x, active[0].b.h).

# Iteration 9
# x: 24
# data: defaultdict(<class 'list'>, {'right': [3]})
# removing candidates...
# start active: [Active(val=-8, b=Building(l=19, r=24, h=8))]
# end active: []
# case 2
# start res: [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8)]
# end res: [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8),
#           (24, 0)]
# Here, we have our final x-coord, 24, which belongs to building 3 and
# is the right edge. Since active[0] is currently building 3 with
# `r` = 24 and since x is currently 24, we pop from the heap. This will
# remove building 3 from the heap (which makes sense since we have
# exhausted building 3). This will now leave our heap empty.
# Since this is a right edge, we don't push to the heap.
# Case 2 is executed since our heap (active) is now empty. We append a
# key point at (24,0) or (x,0) since we have exhausted all candidate
# buildings and this is the end of this chunk of the skyline.

# FINAL RESULT: [(2, 10), (3, 15), (7, 12), (12, 0), (15, 10), (20, 8),
#                (24, 0)]

import heapq
import itertools
from collections import defaultdict, namedtuple
from typing import List, Tuple

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

Building = namedtuple('Building', ('l', 'r', 'h'))
Active = namedtuple('Active', ('val', 'b'))


def gather_skyline_keypoints(buildings: List[List[int]]) -> List[Tuple[int, int]]:
    ##########
    # Step 1 #
    ##########
    # x-coordinates to scan through (to be sorted later on)
    scan = defaultdict(lambda: defaultdict(list))

    # Instantiate list of buildings as namedtuples
    B = []

    for b_idx, b in enumerate(buildings):
        l, r, h = b

        # Collect building defns
        B.append(Building(l, r, h))

        # Store x-coord as key and value as left or right with value as
        # building index
        # [(2, {'left': [0]})] means x-coord 2 is left edge of building 0
        # [(7, {'right': [2]})] means x-coord 7 is right edge of building 2
        scan[l]['left'].append(b_idx)
        scan[r]['right'].append(b_idx)

    # Sort based on x-coords
    scan = sorted(scan.items())

    #####################
    # Step 2 and Step 3 #
    #####################
    # List to keep track of candidates (heap)
    active: List[Active] = []

    # List to store key points (result)
    res: List[Tuple[int, int]] = []

    for x, data in scan:
        # Remove candidate buildings once "exhausted"
        while active and active[0].b.r <= x:
            heapq.heappop(active)

        # Append "incoming" candidates
        # Append only left edges to active buildings
        # Active meaning not exhausted
        # (i.e. haven't reached buildings right edge yet)
        for b_idx in data['left']:
            heapq.heappush(active, Active(-B[b_idx].h, B[b_idx]))
        # Case 1:
        # Examining first x-coordinate, we simply add
        # new key point based on top candidate
        if not res:
            res.append((x, active[0].b.h))

        # Case 2:
        # No more candidates, key point at 0
        elif not active:
            res.append((x, 0))

        # Case 3:
        # Top candidate's height differs from
        # preceding key point, add new key point
        elif active[0].b.h != res[-1][1]:
            res.append((x, active[0].b.h))

    return res


######################
# Plotting Utilities #
######################
def plot_skyline(buildings: List[List[int]]):
    # Get color cycle so each building is different color
    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']
    colors_cycle = itertools.cycle(colors)

    fig = plt.figure()
    ax = fig.add_subplot()  # nrows=1, ncols=1, index=1

    zorder = len(buildings)

    for building, color in zip(buildings, colors_cycle):
        ax.add_patch(
            Rectangle(
                xy=(building[0], 0),
                width=building[1] - building[0],
                height=building[2],
                edgecolor='black',
                facecolor=color,
                fill=True,
                zorder=zorder,
            )
        )

        zorder -= 1

    plt.xlim([0, max(b[1] for b in buildings) + 1])
    plt.ylim([0, max(b[2] for b in buildings) + 1])

    plt.title('Skyline Plot')

    return fig


def plot_skyline_with_keypoints(buildings, keypoints):
    fig = plt.figure()
    ax = fig.add_subplot()  # nrows=1, ncols=1, index=1

    for keypoint in keypoints:
        ax.scatter(keypoint[0], keypoint[1], color='red')

    for building in buildings:
        ax.add_patch(
            Rectangle(
                xy=(building[0], 0),
                width=building[1] - building[0],
                height=building[2],
                fill=True,
                zorder=0,  # skyline behind points (lower order drawn first)
            )
        )

    plt.xlim([0, max(b[1] for b in buildings) + 1])
    plt.ylim([0, max(b[2] for b in buildings) + 1])

    plt.title(f'Skyline Plot with {len(keypoints)} Key Points')

    return fig
