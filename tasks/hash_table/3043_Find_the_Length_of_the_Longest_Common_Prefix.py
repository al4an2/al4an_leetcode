class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefix_set = set()
        ans = 0

        for num in arr1:
            prefix = num
            while prefix > 0:
                prefix_set.add(prefix)
                prefix = prefix // 10
            
        for el in arr2:
            numb = el
            while numb > 0:
                if numb in prefix_set:
                    ans = max(ans, len(str(numb)))
                    break
                numb = numb // 10
        
        return ans