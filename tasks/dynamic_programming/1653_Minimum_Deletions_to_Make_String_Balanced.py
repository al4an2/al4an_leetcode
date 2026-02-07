class Solution:
    def minimumDeletions(self, s: str) -> int:
        
        dp_a = 0
        dp_ab = 0

        for c in s:
            if c == 'a':
                dp_ab = min(dp_ab + 1, dp_a)
            else:
                dp_a += 1
        
        return dp_ab

                
            
