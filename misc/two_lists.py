"""
Practice Problem:

Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a function that returns a list that contains only the
elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
"""


def compare_lists(a, b):
    """
    Take two lists and return a list of unique values that are common
    between the two lists.

    Args
        a (list): The first list.
        b (list): The second list.

    Returns
        in_common (list): A list of elements common between a and b.
    """
    in_common = list(set(a).intersection(b))
    return in_common


if __name__ == "__main__":
    list_1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    in_common = compare_lists(list_1, list_2)
    print("{} is the intersection of {} and {}".format(in_common, list_1, list_2))

    list_3 = [1, 1, 1]
    list_4 = [1, 2, 3, 4, 5]
    in_common = compare_lists(list_3, list_4)
    print("{} is the intersection of {} and {}".format(in_common, list_3, list_4))
