#defdict
from collections import defaultdict


class Solution2:
    def maximumLengthSubstring(self, s: str) -> int:
        st = 0
        fn = 0

        hash_dict = defaultdict(int)
        ans = 0

        while fn < len(s):
            hash_dict[s[fn]] += 1
            while hash_dict[s[fn]] > 2:
                hash_dict[s[st]] -=1
                st +=1
            ans = max(ans, fn - st + 1)
            fn += 1
        
        return ans
    

#counter 26
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        st = 0

        count = [0] * 26
        ans = 0

        for idx, n in enumerate(s):
            char = ord(n) - ord('a')
            count[char] += 1
            while count[char] > 2:
                count[ord(s[st]) - ord('a')] -= 1
                st +=1
            ans = max(ans, idx - st + 1)
        
        return ans
    