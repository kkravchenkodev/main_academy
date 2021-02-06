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


def studying_hours(a):
    if a == sorted(a):
        return len(a)


a = [2, 3, 4, 5, 1, 3, 2, 4, 5, 6, 2, 6, 7, 5, 2, 7, 5, 6, 2]
a = [2, 2, 1, 1, 3, 4, 1]


def find_longest_array(array):
    start = 0
    end = 0
    for left in range(len(array)):
        for right in range(left + 1, len(array)):
            sub_array = array[left:right + 1]
            if sorted(sub_array) == sub_array:
                if len(sub_array) > end - start:
                    start, end = left, right
                if end == len(array):
                    return start, end
            else:
                break
    return len(a[start:end])


# print(find_longest_array(a))


list = [1, 5, 78, 2, 3, 6, 8, 1, 7, 2, 9, 3, 7, 2]


# print(list)
# length = 0
# for index, item in enumerate(list):
#     a = item
#     for index2, following in enumerate(list[index:]):
#         b = following
#         if sorted([a, b]) != [a, b]:  # comparison here, looking for break in pattern
#             if index2 > length:
#                 length = index2
#                 start = index
#             break
#         a = b  # update current value to continue
#
# print("Sequence {} long, between {} and {}".format(length, start, start + length - 1))
# print(list[start:start + length])

def find_longest_array2(a):
    l_start = l_end = start = 0
    for idx, item in enumerate(a):
        if idx:
            if a[idx - 1] > item:
                start = idx
            elif idx - start > l_end - l_start:
                l_start, l_end = start, idx
    return len(a[l_start: l_end + 1])


print(find_longest_array2(a))
"""
	Test	Expected	Got	
print(studying_hours([2, 2, 1, 3, 4, 1]))
3
3
print(studying_hours([2, 2, 9]))
3
3
print(studying_hours([10, 100, 111, 1, 2]))
3
3
print(studying_hours(
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
50
50
print(studying_hours(
    [1, 638, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
     1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 655, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
     1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
     1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1, 27, 533, 1000, 1000, 1000, 1000, 1000, 1000, 1000,
     1000, 1000, 1000, 1000, 1000, 1000, 1, 835, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1,
     992]))
42
42
"""