class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        prev_group = 0
        curr_group = 1


        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev_group, curr_group)
                prev_group = curr_group
                curr_group = 1
            else:
                curr_group += 1
        
        return ans + min(prev_group, curr_group) #don't forget
    

#easier - with grouping

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = [1]
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                res.append(1)
            else:
                res[-1] += 1

        ans = 0
        for i in range(1,len(res)):
            ans += min(res[i-1], res[i])
        
        return ans