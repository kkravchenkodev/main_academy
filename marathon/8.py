"""
's3ooOOooDy' has exams. He wants to study hard this time. He has an array of studying hours per day for the previous exams.
He wants to know the length of the maximum non-decreasing contiguous subarray of the studying days, to study as much before his current exams.

Example:
For a = [2,2,1,3,4,1] the answer is 3.
[input] array.integer a
The number of hours he studied each day.
[output] integer
The length of the maximum non-decreasing contiguous subarray.
"""


# a = [2, 3, 4, 5, 1, 3, 2, 4, 5, 6, 2, 6, 7, 5, 2, 7, 5, 6, 2]
# a = [2, 2, 1, 1, 3, 4, 1]
# a = [1, 5, 78, 2, 3, 6, 8, 1, 7, 2, 9, 3, 7, 2]


def find_longest_array(a):
    l_start = l_end = start = 0
    for idx, item in enumerate(a):
        if idx:
            if a[idx - 1] > item:
                start = idx
            elif idx - start > l_end - l_start:
                l_start, l_end = start, idx
    return len(a[l_start: l_end + 1])

if __name__ == '__main__':
    assert find_longest_array([2, 2, 1, 3, 4, 1]) == 3
    assert find_longest_array([2, 2, 9]) == 3
    assert find_longest_array([10, 100, 111, 1, 2]) == 3
    assert find_longest_array(
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 50
    assert find_longest_array(
        [1, 638, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
         1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 655, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
         1000,
         1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
         1000,
         1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 27, 533, 1000, 1000, 1000, 1000, 1000,
         1000,
         1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 835, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
         1000,
         1, 992]) == 42
