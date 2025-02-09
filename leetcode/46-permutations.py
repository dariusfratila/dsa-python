"""
@complexity
time: O(n!)
space: O(n)
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(current_list):
            if len(current_list) == len(nums):
                res.append(current_list.copy())
                return

            for num in nums:
                if num in current_list:
                    continue

                current_list.append(num)
                dfs(current_list)
                current_list.pop()

        dfs([])
        return res
