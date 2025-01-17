"""
@complexity
time: O(n)
space: O(n)
"""

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: #type: ignore
        freq_hash = Counter(nums)
        count = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_hash.items():
            count[freq].append(num)

        output = []
        for index in range(len(nums), 0, -1):
            for j in count[index]:
                output.append(j)
                if len(output) == k:
                    return output
