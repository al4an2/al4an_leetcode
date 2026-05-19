class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        left, right = 0, len(nums1)
        half = (len(nums1) + len(nums2) + 1)//2

        while left <= right:
            i = left + (right - left) // 2

            j = half - i

            l1 = nums1[i-1] if i > 0 else float("-inf")
            r1 = nums1[i] if i < len(nums1) else float("inf")
            l2 = nums2[j-1] if j > 0 else float("-inf")
            r2 = nums2[j] if j < len(nums2) else float("inf")

            if l1 > r2:
                right = i - 1
            elif l2 > r1:
                left = i + 1
            else:
                if (len(nums1) + len(nums2)) % 2 != 0:
                    return max(l1,l2)
                else:
                    return (max(l1,l2) + min(r1,r2)) / 2