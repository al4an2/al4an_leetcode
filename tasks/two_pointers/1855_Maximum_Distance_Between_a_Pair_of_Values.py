#binsearch

class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        max_distance = 0
        n,m = len(nums1), len(nums2)

        for i in range(n):
            left, right = i, m-1
            pos = 0
            while left <= right:
                mid = (left + right) // 2

                if nums2[mid] < nums1[i]:
                    right = mid - 1
                else:
                    left = mid + 1
                    max_distance = max(max_distance, mid - i)
        
        return max_distance

#two pointers
class Solution:
    def maxDistance(self, nums1: list[int], nums2: list[int]) -> int:
        max_distance = 0
        j = 0
        i = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                max_distance = max(max_distance, j - i)
                j += 1
            else:
                i += 1
                if j < i:
                    j += 1
                
        return max_distance
