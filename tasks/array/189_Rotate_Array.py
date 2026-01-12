#pythonic-style
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        nums[:] = nums[-k:] + nums[:-k]

#interview-style
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums) 
        k %= n
        start = moved = 0 
        
        while moved < n:
            current, prev = start, nums[start]
            while True:
                nxt = (current + k) % n
                nums[nxt], prev = prev, nums[nxt]
                current = nxt
                moved +=1

                if current == start:
                    break

            start += 1

