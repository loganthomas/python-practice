# My first attempt
def binary_search(x, find):
    mid_idx = len(x) // 2
    if not x:
        return -1
    if x[mid_idx] == find:
        return find
    if find < x[mid_idx]:
        end = mid_idx - 1
        found = binary_search(x[: end + 1], find)
    if find > x[mid_idx]:
        start = mid_idx + 1
        found = binary_search(x[start:], find)

    return found


x = list(range(9))
binary_search(x, 8)


# Revised
def binary_search2(x, low, high, find):
    if high >= low:
        mid = (high + low) // 2

        if x[mid] == find:
            return find
        elif find < x[mid]:
            return binary_search2(x, low, mid - 1, find)
        else:
            return binary_search2(x, mid + 1, high, find)
    else:
        return -1


x = list(range(9))
binary_search2(x, 0, len(x) - 1, 8)


def binary_search_enum(x, low, high, find):
    """
    assumes x in enumerated [(0, x1), (1, x2)...]
    """
    if high >= low:
        mid = (high + low) // 2

        if x[mid][1] == find:
            return x[mid]
        elif find < x[mid][1]:
            return binary_search_enum(x, low, mid - 1, find)
        else:
            return binary_search_enum(x, mid + 1, high, find)
    else:
        return -1


x = list(range(9))
# binary search assumes sorted to begin with but just to make sure...
x_enum = sorted(enumerate(x))
binary_search_enum(x_enum, 0, len(x_enum) - 1, 8)
