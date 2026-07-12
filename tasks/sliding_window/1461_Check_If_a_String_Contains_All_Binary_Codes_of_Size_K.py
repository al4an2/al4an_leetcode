class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        set_ = set()

        for i in range(len(s)-k+1):
            set_.add(s[i:i+k])
        
        return len(set_) == 2**k
