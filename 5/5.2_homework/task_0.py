# way 1
# number = int(input())
# num_list = []
# while number != 0:
#     ost = number % 10
#     num_list.append(str(ost))
#     number = number // 10
#
# print('=' * 50)
# num_list.sort()
# print(''.join(num_list))
# num_list.sort(reverse=True)
# print(''.join(num_list))


# way 2
number = input()
nums = [item for _, item in enumerate(number) if item.isdigit()]
print('=' * (20 + len(nums)))
print('Min number is ->', ''.join(sorted(nums)))
print('=' * (20 + len(nums)))
print('Max number is ->', ''.join(sorted(nums, reverse=True)))
