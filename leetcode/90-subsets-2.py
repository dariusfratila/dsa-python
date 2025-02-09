"""
@complexity
time: O(2^n)
space: O(n)
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(index, current_list):
            if index == len(nums):
                res.append(current_list.copy())
                return

            current_list.append(nums[index])
            dfs(index + 1, current_list)

            current_list.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            dfs(index + 1, current_list)

        dfs(0, [])
        return res
