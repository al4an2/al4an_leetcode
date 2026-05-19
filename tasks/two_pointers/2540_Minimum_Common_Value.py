#two pointers
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        n1, n2 = len(nums1) - 1, len(nums2) - 1
        p1, p2 = 0, 0
        while p1 <= n1 and p2 <= n2:
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            
            if nums1[p1] < nums2[p2]:
                p1 +=1
            else:
                p2 +=1
        return -1
    
#two_sets
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        comm_nums = set(nums1).intersection(set(nums2))
        return min(comm_nums) if comm_nums else -1
    
#set
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        set_nums = set(nums1)

        for num in nums2:
            if num in set_nums:
                return num

        return -1