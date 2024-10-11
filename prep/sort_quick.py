"""
Quick Sort
-----------
Pick a random element and partition the array, such that all numbers
that are less than the partitioning element come before all elements
that are greater than it. The partitioning can be performed efficiently
through a series of swaps.

If we repeatedly partition the array (and its sub-arrays) around an
element, the array will eventually become sorted. However, as the
partitioned element is not guaranteed to be the median (or anywhere
near the median), our sorting could be very slow. This is the reason
for O(n**2) worst case runtime

Runtime: O(n*log(n)) average O(n**2) worst case
Memory: O(log(n))

Great Resource:
https://www.programiz.com/dsa/quick-sort
"""
# Quick sort in Python


# Function to partition the array on the basis of pivot element
def partition(array, low, high):
    # Select the pivot element
    pivot = array[high]
    print(f'low:{low} high:{high} pivot:{pivot}')
    i = low - 1

    # Put the elements smaller than pivot on the left and greater
    # than pivot on the right of pivot
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    print(array)
    return i + 1


def quickSort(array, low, high):
    if low < high:
        # Select pivot position and put all the elements smaller
        # than pivot on left and greater than pivot on right
        pi = partition(array, low, high)
        print(pi)

        # Sort the elements on the left of pivot
        quickSort(array, low, pi - 1)

        # Sort the elements on the right of pivot
        quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
