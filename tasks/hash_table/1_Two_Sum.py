class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()
        for i in range(len(nums)):
            possible_pare = target - nums[i]
            if possible_pare in hashtable:
                return [hashtable[possible_pare], i]
            hashtable[nums[i]] = i
        
        return -1