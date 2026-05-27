class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = [-1] * 26
        upper = [-1] * 26

        for idx, el in enumerate(word):
            if el.islower():
                lower[ord(el) - ord("a")] = idx
            elif upper[ord(el) - ord("A")] == -1:
                upper[ord(el) - ord("A")] = idx
            
        counter = 0
        for idx in range(26):
            if lower[idx] < upper[idx] and lower[idx] != -1:
                counter += 1

        return counter