class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_subsring = 0
        now_in_s = set()

        for right in range(len(s)):

            while s[right] in now_in_s:
                now_in_s.remove(s[left])
                left += 1

            now_in_s.add(s[right])
            max_subsring = max(max_subsring, right - left + 1)
        
        return max_subsring