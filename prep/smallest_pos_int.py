"""
Smallest Positive Integer
-------------------------
Write a function, solution(A), that, given an array A of N integers,
returns the smallest positive integer (greater than 0) that does not
occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [-1, -3], the function should return 1.

Write an *efficient* algorithm for the following assumptions:
    - N is an integer in the range[1..100,000]
    - Each element of array A is an integer within the range
      [-1,000,000 ... 1,000,000].
"""


# Brute Force
def brute_solution(A):
    for x in range(1, 100_001):
        if x not in set(A):
            return x


# Better
def better_solution(A):
    n = len(A)
    opts = set(range(1, n + 2))
    return min(opts - set(A))


# Best
def solution(A):
    set_A = set(A)
    ans = 1
    while ans in set_A:
        ans += 1
    return ans


# >>> A = [1, 3, 6, 4, 1, 2]
# >>> %timeit brute_solution(A)
# 1.08 µs ± 16.6 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
# >>> %timeit better_solution(A)
# 733 ns ± 8.75 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)
# >>> %timeit solution(A)
# 344 ns ± 2.83 ns per loop (mean ± std. dev. of 7 runs, 1,000,000 loops each)

# >>> A = list(range(1,10_000))
# >>> %timeit brute_solution(A)
# 1.09 s ± 7.34 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
# >>> %timeit better_solution(A)
# 489 µs ± 8.17 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
# >>> %timeit solution(A)
# 570 µs ± 4.57 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
