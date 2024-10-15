"""
https://www.youtube.com/watch?v=21pmwl0hrME

Given a set of numbers, find a pair of numbers that add up to a certain target.

Example: Given [1,2,3,9] and target of 10, identify that 1 and 9 add up to 10.

Other details:
- Can have a target that does not exist (like 8 in the above).
- Assume the array is sorted.
- Assume only integers (positive and negative) and no floating point numbers.
- Duplicate elements (only one 4 exists), cannot add to itself but
  can have duplicate numbers at different indexes ([1,4] vs [1, 4, 4]).
"""

# Test cases
# a = [1,2,3,9], target=10
# a = [1,4,4], target=8
# a = [1,4], target=8


# Brute force O(N**2)
def find_sum_to_target(a, target):
    for i in range(len(a) - 1):
        for j in range(i + i, len(a)):
            if a[i] + a[j] == target:
                return True
    return False


# Brute force O(N**2)
def find_sum_to_target2(a, target):
    for i in range(len(a) - 1):
        for j in range(i + i, len(a)):
            if a[i] + a[j] == target:
                return a[i], a[j]
    return -1


# Elements are sorted so using that information can do binary search
# Find compliment (if target=8 and start with first element (1) then
# compliment is 7) and binary search rest of array for compliment.


# Compliment Search using binary search O(N*logN)
# (logN for binary search and perform search N times)
def binary_search(x, low, high, target):
    if high >= low:
        mid = (low + high) // 2
        if x[mid] == target:
            return target
        elif x[mid] > target:
            return binary_search(x, low, mid - 1, target)
        else:
            return binary_search(x, mid + 1, high, target)
    else:
        return -1


def find_sum_to_target_w_binary_search(a, target):
    for i, n in enumerate(a):
        comp = target - n
        search_result = binary_search(a[i + 1 :], 0, len(a[i + 1 :]) - 1, comp)
        if search_result != -1:
            return (n, search_result)
    return -1


# Can you get to something linear?
# Because things are sorted...
# Last two elements of the array would give biggest possible sum
# First two elements of the array would give the smallest possible sum
# Use two indices, one at start and one at end, and sum.
# If the sum is greater than target, need a smaller sum so move high down
# If the sum is less than target, need a bigger sum so move low up


# This would be O(N) since iterating through numbers once
def find_sum_to_target_w_indexing(a, target):
    low, high = 0, len(a) - 1

    # since a number can't use itself, this needs to be strictly less than
    # if <=, the [1,4] would return (4,4) which is incorrect
    while low < high:
        sum_ = a[low] + a[high]

        if sum_ == target:
            return a[low], a[high]
        elif sum_ > target:
            high -= 1
        else:
            low += 1
    return -1


# Now assume the collection of numbers is not sorted, how would you solve this?
# If not sorted the indexing won't work, have to go back to the compliment idea.
# Could sort it and the use the above (would be O(N*logN)).
# Since the array is no longer sorted, binary search won't work with the compliment idea,
# so need something else.

# Example: a = [1,2,3,9,22], target = 10
# Start with n = 1 and comp = 9 (looking for a 9)
# If I know I've seen a 7 before, I can use that information to limit searching.
# Data structure to easily look up elements
# If I know I've seen a 7 before, I can use that information to limit searching.
# Data structure to easily look up elements quickly (hash table, set?)
# Don't really need key, value pairs since we just care about what numbers we've seen.
# Approach: scan through values, have we seen compliment before, if so return, else add to comp set.


def find_sum_to_target_w_set(a, target):
    comps = set()
    for n in a:
        comp = target - n
        if n in comps:
            return n, comp
        else:
            comps.add(comp)
    return -1
