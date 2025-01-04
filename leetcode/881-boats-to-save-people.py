"""
@complexity
time: O(nlogn)
space: O(1)
"""


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0

        while l <= r:
            if l == r:
                boats += 1
                break
            if people[l] + people[r] <= limit:
                boats += 1
                r -= 1
                l += 1
            else:
                boats += 1
                r -= 1

        return boats
