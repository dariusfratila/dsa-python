"""
@complexity
time: O(2^n)
space: O(n)
"""


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(index, current_list, current_sum):
            if current_sum == target:
                res.append(current_list.copy())
                return

            if current_sum > target or index >= len(candidates):
                return

            current_list.append(candidates[index])
            dfs(index + 1, current_list, current_sum + candidates[index])
            current_list.pop()

            next_index = index + 1
            while next_index < len(candidates) and candidates[next_index] == candidates[index]:
                next_index += 1

            dfs(next_index, current_list, current_sum)

        dfs(0, [], 0)
        return res
