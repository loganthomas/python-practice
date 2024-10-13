"""
https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/description/?envType=daily-question&envId=2024-10-12

You are given a 2D integer array intervals where intervals[i] = [lefti, righti]
represents the inclusive interval [lefti, righti].

You have to divide the intervals into one or more groups
such that each interval is in exactly one group,
and no two intervals that are in the same group intersect each other.

Return the minimum number of groups you need to make.

Two intervals intersect if there is at least one common number between them.
For example, the intervals [1, 5] and [5, 8] intersect.



Example 1:

Input: intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
Output: 3
Explanation: We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.
Example 2:

Input: intervals = [[1,3],[5,6],[8,10],[11,13]]
Output: 1
Explanation: None of the intervals overlap, so we can put all of them in one group.


Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 106


Hints:
Can you find a different way to describe the question?
The minimum number of groups we need is equivalent to
the maximum number of intervals that overlap at some point. How can you find that?
"""

import heapq


def min_groups_1(intervals):
    intervals.sort()
    pq = []
    for start, end in intervals:
        if pq and pq[0] < start:
            heapq.heappop(pq)
        heapq.heappush(pq, end)
    return len(pq)


def min_groups_2(intervals):
    start_times = sorted(i[0] for i in intervals)
    end_times = sorted(i[1] for i in intervals)
    end_ptr, group_count = 0, 0

    for start in start_times:
        if start > end_times[end_ptr]:
            end_ptr += 1
        else:
            group_count += 1

    return group_count


#######################################################################
# Failed attempt 1
#######################################################################
# def check_membership(check_interval, groups):
#     available = []
#     for i, group in enumerate(groups):
#         exclusion = []
#         for interval in group:
#             if check_interval[0] in interval or check_interval[1] in interval:
#                 exclusion.append(1)
#             else:
#                 exclusion.append(0)
#         if not any(exclusion):
#             available.append(i)
#     return min(available) if available else None


# def handle_membership(check_interval, available, groups):
#     if available is None:
#         groups.append([range(check_interval[0], check_interval[1] + 1)])
#     else:
#         groups[available].append(range(check_interval[0], check_interval[1] + 1))
#     return groups


# class Solution:
#     def minGroups(self, intervals: List[List[int]]) -> int:
#         groups = []

#         for interval in intervals:
#             if not groups:
#                 groups.append([range(interval[0], interval[1] + 1)])
#             else:
#                 idx = check_membership(interval, groups)
#                 groups = handle_membership(interval, idx, groups)
#         return len(groups)


# # Failed test case
# # [[159431,428743],[614908,651142],[431031,806494]]
# # expected = 2
# # output = 1
#######################################################################


#######################################################################
# Failed attempt 2
#######################################################################
# def check_membership(check_interval, groups):
#     available = []
#     for i, group in enumerate(groups):
#         exclusion = []
#         for interval in group:
#             # this is bad... but brute force for now
#             # need to check both ways
#             conditions = (
#                 check_interval[0] in range(interval[0], interval[1] + 1)
#                 or check_interval[1] in range(interval[0], interval[1] + 1)
#                 or interval[0] in range(check_interval[0], check_interval[1] + 1)
#                 or interval[1] in range(check_interval[0], check_interval[1] + 1)
#             )
#             if conditions:
#                 exclusion.append(1)
#             else:
#                 exclusion.append(0)
#         if not any(exclusion):
#             available.append(i)
#     return min(available) if available else None


# def handle_membership(check_interval, available, groups):
#     if available is None:
#         groups.append([(check_interval[0], check_interval[1])])
#     else:
#         groups[available].append((check_interval[0], check_interval[1]))
#     return groups


# class Solution:
#     def minGroups(self, intervals: List[List[int]]) -> int:
#         groups = []

#         for interval in intervals:
#             if not groups:
#                 groups.append([(interval[0], interval[1])])
#             else:
#                 available = check_membership(interval, groups)
#                 groups = handle_membership(interval, available, groups)
#         return len(groups)


# # Wrong answer expected 19, got 20
# intervals = [
#     [229966, 812955],
#     [308778, 948377],
#     [893612, 952735],
#     [395781, 574123],
#     [478514, 875165],
#     [766513, 953839],
#     [460683, 491583],
#     [133951, 212694],
#     [376149, 838265],
#     [541380, 686845],
#     [461394, 568742],
#     [804546, 904032],
#     [422466, 467909],
#     [557048, 758709],
#     [680460, 899053],
#     [110928, 267321],
#     [470258, 650065],
#     [534607, 921875],
#     [292993, 994721],
#     [645020, 692560],
#     [898840, 947977],
#     [33584, 330630],
#     [903142, 970252],
#     [17375, 626775],
#     [804313, 972796],
#     [582079, 757160],
#     [785002, 987823],
#     [599263, 997719],
#     [486500, 527956],
#     [566481, 813653],
#     [211239, 863969],
#     [808577, 883125],
#     [21880, 516436],
#     [264747, 412144],
#     [327175, 772333],
#     [984807, 988224],
#     [758172, 916673],
#     [23583, 406006],
#     [954674, 956043],
#     [379202, 544291],
#     [688869, 785368],
#     [841735, 983869],
#     [99836, 916620],
#     [332504, 740696],
#     [740840, 793924],
#     [896607, 920924],
#     [868540, 922727],
#     [125849, 550941],
#     [433284, 685766],
# ]

#######################################################################


#######################################################################
# Failed attempt 3
#######################################################################
# import itertools
# import operator
# import numpy as np


# class Solution:
#     def minGroups(self, intervals: List[List[int]]) -> int:
#         start_times, end_times = list(zip(*intervals))
#         time_mapping = {**{t: 1 for t in start_times}, **{t: -1 for t in end_times}}
#         time_signs = [time_mapping[t] for t in sorted(start_times + end_times)]
#         # np.max(np.add.accumulate(time_signs))
#         # return max(itertools.accumulate(time_signs, operator.add))
#         return np.max(np.add.accumulate(time_signs))

#######################################################################
