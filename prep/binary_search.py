"""
Practice manually implementing a binary search.

Binary Search Algorithm is a searching algorithm used in a
*sorted array* by repeatedly dividing the search interval in half.

The idea of binary search is to use the information that
the array is sorted and reduce the time complexity to O(log N).

References
----------
https://www.geeksforgeeks.org/binary-search/
"""

# def binary_search(x, find):
#     """
#     First attempt
#     """
#     mid_idx = len(x) // 2
#     if not x:
#         return -1
#     if x[mid_idx] == find:
#         return find
#     if find < x[mid_idx]:
#         end = mid_idx - 1
#         found = binary_search(x[: end + 1], find)
#     if find > x[mid_idx]:
#         start = mid_idx + 1
#         found = binary_search(x[start:], find)

#     return found


def binary_search_recursive(x, low, high, find):
    """
    Revised
    """
    if high >= low:
        mid = (high + low) // 2

        if x[mid] == find:
            return find
        elif find < x[mid]:
            return binary_search_recursive(x, low, mid - 1, find)
        else:
            return binary_search_recursive(x, mid + 1, high, find)
    else:
        return -1


def binary_search_indexed(x, low, high, find):
    """
    assumes x in enumerated [(0, x1), (1, x2)...]
    """
    if high >= low:
        mid = (high + low) // 2

        if x[mid][1] == find:
            return x[mid]
        elif find < x[mid][1]:
            return binary_search_indexed(x, low, mid - 1, find)
        else:
            return binary_search_indexed(x, mid + 1, high, find)
    else:
        return -1


def binary_search_iterative(x, low, high, find, show_index=False):
    while high >= low:
        mid = low + (high - low) // 2

        if x[mid] == find:
            return (mid, find) if show_index else find
        elif find < x[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
