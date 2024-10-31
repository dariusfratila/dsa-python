"""
@complexity
time: O(n * k * log x)
space: O(k)
"""


class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        freq = Counter(nums[:k])
        res = []

        def calculate_x_sum(counter):
            topX = heapq.nlargest(x, counter.items(),
                                  key=lambda item: (item[1], item[0]))
            return sum(val * count for val, count in topX)

        res.append(calculate_x_sum(freq))

        for index in range(1, len(nums) - k + 1):
            freq[nums[index - 1]] -= 1
            if freq[nums[index] - 1] == 0:
                del freq[nums[index] - 1]

            freq[nums[index + k - 1]] += 1

            res.append(calculate_x_sum(freq))

        return res
