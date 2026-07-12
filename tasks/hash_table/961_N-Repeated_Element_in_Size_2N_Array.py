class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        hash_d = set()
        for el in nums:
            if el in hash_d:
                return el
            hash_d.add(el)
