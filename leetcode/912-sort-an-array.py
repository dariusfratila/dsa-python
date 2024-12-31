"""
@complexity
time: O(nlogn)
space: O(n)
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = len(nums) // 2
        left_list = self.sortArray(nums[:pivot])
        right_list = self.sortArray(nums[pivot:])
        return self.merge(left_list, right_list)

    def merge(self, left_list, right_list):
        result = []
        left_pointer, right_pointer = 0, 0
        while left_pointer < len(left_list) and right_pointer < len(right_list):
            if left_list[left_pointer] < right_list[right_pointer]:
                result.append(left_list[left_pointer])
                left_pointer += 1
            else:
                result.append(right_list[right_pointer])
                right_pointer += 1

        result.extend(left_list[left_pointer:])
        result.extend(right_list[right_pointer:])

        return result
