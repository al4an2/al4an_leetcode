class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s = set(word)

        count = 0

        for i in range(26):
            char = chr(ord('a') + i)
            if char in s and char.upper() in s:
                count += 1
        
        return count