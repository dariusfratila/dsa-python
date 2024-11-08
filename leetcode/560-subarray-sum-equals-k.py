"""
@complexity
time: O(n)
space: O(n)
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hash = {0: 1}

        curSum, res = 0, 0
        for num in nums:
            curSum += num

            if curSum - k in hash:
                res += hash[curSum - k]

            hash[curSum] = 1 + hash.get(curSum, 0)

        return res
