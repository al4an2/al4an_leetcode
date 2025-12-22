from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
            dict_n = defaultdict(int)
            res = 0
            prefix_sum = 0

            dict_n[0] = 1

            for el in nums:
                prefix_sum += el

                if prefix_sum - k in dict_n:
                    res += dict_n[prefix_sum - k]

                dict_n[prefix_sum] += 1
            return res