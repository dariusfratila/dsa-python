"""
@complexity
time: O(n)
space: O(1)
"""


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruitHash = {}
        left = 0
        window = 0
        for right in range(len(fruits)):
            fruitHash[fruits[right]] = 1 + fruitHash.get(fruits[right], 0)

            while len(fruitHash) > 2:
                fruitHash[fruits[left]] -= 1
                if fruitHash[fruits[left]] == 0:
                    del fruitHash[fruits[left]]
                left += 1

            window = max(window, right - left + 1)

        return window
