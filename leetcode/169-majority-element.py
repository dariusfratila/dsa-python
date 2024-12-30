"""
@complexity
time: O(n)
space: O(n)
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = -1
        ans = -1

        counter = Counter(nums)
        for key, val in counter.items():
            if val > max_count:
                max_count = val
                ans = key

        return ans


"""
follow-up:
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num

            if ans == num:
                count += 1
            else:
                count -= 1

        return ans
