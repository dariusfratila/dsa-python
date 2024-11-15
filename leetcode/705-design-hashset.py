"""
@complexity
time: O(1)
space: O(n)
"""


class MyHashSet(object):

    def __init__(self):
        self.num_buckets = 1000
        self.buckets = [[] for _ in range(self.num_buckets)]

    def hash_function(self, key):
        return key % self.num_buckets

    def is_in_bucket(self, key, index):
        return key in self.buckets[index]

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """

        index = self.hash_function(key)
        if not self.is_in_bucket(key, index):
            self.buckets[index].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """

        index = self.hash_function(key)
        if self.is_in_bucket(key, index):
            self.buckets[index].remove(key)

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """

        index = self.hash_function(key)
        return self.is_in_bucket(key, index)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
