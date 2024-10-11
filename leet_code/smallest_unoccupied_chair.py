"""
https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/description/?envType=daily-question&envId=2024-10-11

1942. The Number of the Smallest Unoccupied Chair

There is a party where n friends numbered from 0 to n - 1 are attending.
There is an infinite number of chairs in this party that are numbered from 0 to infinity.
When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave.
If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi],
indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend.
All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.



Example 1:

Input: times = [[1,4],[2,3],[4,6]], targetFriend = 1
Output: 1
Explanation:
- Friend 0 arrives at time 1 and sits on chair 0.
- Friend 1 arrives at time 2 and sits on chair 1.
- Friend 1 leaves at time 3 and chair 1 becomes empty.
- Friend 0 leaves at time 4 and chair 0 becomes empty.
- Friend 2 arrives at time 4 and sits on chair 0.
Since friend 1 sat on chair 1, we return 1.
Example 2:

Input: times = [[3,10],[1,5],[2,6]], targetFriend = 0
Output: 2
Explanation:
- Friend 1 arrives at time 1 and sits on chair 0.
- Friend 2 arrives at time 2 and sits on chair 1.
- Friend 0 arrives at time 3 and sits on chair 2.
- Friend 1 leaves at time 5 and chair 0 becomes empty.
- Friend 2 leaves at time 6 and chair 1 becomes empty.
- Friend 0 leaves at time 10 and chair 2 becomes empty.
Since friend 0 sat on chair 2, we return 2.


Constraints:

n == times.length
2 <= n <= 104
times[i].length == 2
1 <= arrivali < leavingi <= 105
0 <= targetFriend <= n - 1
Each arrivali time is distinct.
"""


# Initial Attempt
# Fails unittest #3
def gen_hash(times, idx):
    return {t[idx]: f'f{i}' for i, t in enumerate(times)}


def get_chair(arrivals, departures, target):
    chairs = {}
    chair = 0
    timer = min(arrivals)

    for a, f in sorted(arrivals.items()):
        while timer <= a:
            if timer in departures:
                chair = chairs.pop(departures[timer])
            else:
                if f == f'f{target}':
                    return chair
                else:
                    chairs[f] = chair
                    chair += 1
            timer += 1


# # Failed this test
# times = [
#     [33889, 98676],
#     [80071, 89737],
#     [44118, 52565],
#     [52992, 84310],
#     [78492, 88209],
#     [21695, 67063],
#     [84622, 95452],
#     [98048, 98856],
#     [98411, 99433],
#     [55333, 56548],
#     [65375, 88566],
#     [55011, 62821],
#     [48548, 48656],
#     [87396, 94825],
#     [55273, 81868],
#     [75629, 91467],
# ]
# targetFriend = 6
# expected = 2

# Provided Solution
from heapq import heappop, heappush


def smallest_chair(times, target):
    """
    Solution Overview
    -----------------
    Sort times by arrival time, and simulate the seat assignment process.
    For every new friend that wants a seat assigned,
    first check whether the arrival time of that friend is
    greater than or equal to the leaving time of some other friends.
    If so, make those seats available.
    Since all arrival times are unique (given in the problem statement),
    we can use arrival time to tell whether we have reached the target friend.
    When we reach the target friend, we return the minimum available seat
    as required (if arrival == times[target][0]: return available[0]).

    Notes
    -----
    Each heap is a priority queue that keeps things sorted accordingly.

    `available` is a min heap of all available seat numbers, i.e., 0, ... n,
    where n is the length of times array, or the maximum possible seats.

    `leave_times` is a min heap of (time when a person will leave, seat number assigned to this person).
    """

    available, leave_times = list(range(len(times))), []
    for arrival, leaving in sorted(times):
        # check for removal first (handle leaving before arriving if equal)
        # if the arrival time of a friend is greater than or equal to
        # leaving time of other friends, make those seats available
        while leave_times and leave_times[0][0] <= arrival:
            heappush(available, heappop(leave_times)[1])
        # each arrival times is distinct
        if arrival == times[target][0]:
            return available[0]
        heappush(leave_times, (leaving, heappop(available)))


# Updated Provided Solution (using PriorityQueue)
from queue import PriorityQueue


def smallest_chair2(times, target):
    available, leave_times = PriorityQueue(), PriorityQueue()

    # dont love that i have to do this
    for a in range(len(times)):
        available.put(a)

    for arrival, leaving in sorted(times):
        # check for removal first (handle leaving before arriving if equal)
        # if the arrival time of a friend is greater than or equal to
        # leaving time of other friends, make those seats available
        while leave_times.queue and leave_times.queue[0][0] <= arrival:
            available.put(leave_times.get()[1])
        # each arrival times is distinct
        if arrival == times[target][0]:
            return available.queue[0]
        leave_times.put((leaving, available.get()))
