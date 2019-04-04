# [581] https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order,
# then the whole array will be sorted in ascending order, too.
def findUnsortedSubarray(nums: 'List[int]') -> int:
    stack, n = [], len(nums)
    l, r = n, 0
    for i in range(n):
        while stack and nums[stack[-1]] > nums[i]:
            l = min(l, stack.pop())
        stack.append(i)

    stack.clear()

    for i in range(n)[::-1]:
        while stack and nums[stack[-1]] < nums[i]:
            r = max(r, stack.pop())
        stack.append(i)

    return r - l + 1 if r - l > 0 else 0