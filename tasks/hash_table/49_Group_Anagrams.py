from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        chars_dict = defaultdict(list)

        for s in strs:
            word = tuple(sorted(s))
            chars_dict[word].append(s)
        
        return list(chars_dict.values())