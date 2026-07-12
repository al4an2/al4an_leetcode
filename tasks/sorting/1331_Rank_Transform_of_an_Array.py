class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        uniq_s = sorted(set(arr))
        dict_rans = {key: index + 1 for index, key in enumerate(uniq_s)}
        ans = []

        for n in arr:
            ans.append(dict_rans[n])
        
        return ans