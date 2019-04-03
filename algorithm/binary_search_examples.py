import bisect


# [367] https://leetcode.com/problems/valid-perfect-square/
# standard scenario
def is_perfect_square(num: 'int') -> 'bool':
    low, high = 1, num // 2
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid == num:
            return True
        elif mid * mid < num:
            low = mid + 1
        else:
            high = mid - 1
    return False


# [33] https://leetcode.com/problems/search-in-rotated-sorted-array/
# variation with rotated sort
def search_in_rotated_sorted_array(nums: 'List[int]', target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        if nums[lo] == target:
            return lo
        if nums[hi] == target:
            return hi
        mid = lo + (hi - lo) // 2
        if nums[mid] == target:
            return mid

        # find the in-order side, and compare in this side
        if nums[lo] < nums[mid]:
            if nums[lo] < target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target < nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


# [374] https://leetcode.com/problems/guess-number-higher-or-lower/
# variation with tri-partition search
def guessNumber(n):
    # fake API
    def guess(num):
        return 0

    low, high = 1, n
    while low <= high:
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
        res1, res2 = guess(mid1), guess(mid2)
        if res1 == 0:
            return mid1
        if res2 == 0:
            return mid2
        elif res1 < 0:
            high = mid1 - 1
        elif res2 > 0:
            low = mid2 + 1
        else:
            low, high = mid1 + 1, mid2 - 1
    return -1


# [374] https://leetcode.com/problems/guess-number-higher-or-lower/
# variation with construct a sorted iterator
def guessNumber1(n):
    # fake API
    def guess(num):
        return 0

    # construct a sorted iterator
    class C: __getitem__ = lambda _, i: -guess(i)

    return bisect.bisect_right(C(), -1, 1, n)


# [635] https://leetcode.com/problems/design-log-storage-system
# variation with application design
class LogSystem:
    def __init__(self):
        self.logs = []
        self.start = '2000:01:01:00:00:00'
        self.end = '2017:12:31:23:59:59'
        self.gra_idx = {"Year": 4, "Month": 7, "Day": 10, "Hour": 13, "Minute": 16, "Second": 19}

    # O(log(n)) to binary search, O(n) to insert, so skip list or black-red tree is a better solution
    def put(self, id: int, timestamp: str) -> None:
        bisect.insort_left(self.logs, (timestamp, id))

    # O(log(n)) to binary search
    def retrieve(self, s: str, e: str, gra: str) -> 'List[int]':
        idx = self.gra_idx[gra]
        lo = bisect.bisect_left(self.logs, (s[:idx] + self.start[idx:], 0))
        hi = bisect.bisect_right(self.logs, (e[:idx] + self.end[idx:], 300))
        return [log[1] for log in self.logs[lo:hi]]


# [240] https://leetcode.com/problems/search-a-2d-matrix-ii/
# variation with in matrix, not the most efficient solution
def searchMatrix(matrix, target):
    if not matrix:
        return False

    def binary_search(start, vertical):
        lo = start
        hi = len(matrix[0]) - 1 if vertical else len(matrix) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if vertical:  # searching a column
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid - 1
                else:
                    return True
            else:  # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True

        return False

    # iterate over matrix diagonals starting in bottom left.
    for i in range(min(len(matrix), len(matrix[0]))):
        vertical_found = binary_search(i, True)
        horizontal_found = binary_search(i, False)
        if vertical_found or horizontal_found:
            return True
    return False
