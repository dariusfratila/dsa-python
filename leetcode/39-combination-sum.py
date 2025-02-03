""""
@complexity
time: O(2^n)
space: O(n)
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, current_list, total_sum):
            if total_sum == target:
                res.append(current_list.copy())
                return

            if index >= len(candidates) or total_sum > target:
                return

            current_list.append(candidates[index])

            dfs(index, current_list, candidates[index] + total_sum)

            current_list.pop()

            dfs(index + 1, current_list, total_sum)

        dfs(0, [], 0)
        return res
