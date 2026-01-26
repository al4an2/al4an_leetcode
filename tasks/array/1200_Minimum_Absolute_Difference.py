class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()

        ans = []
        min_diff = float("inf")
        for i in range(len(arr)-1):
            diff = arr[i+1] - arr[i]
            if diff == min_diff:
                ans.append([arr[i], arr[i+1]])
            elif diff < min_diff:
                ans = [[arr[i], arr[i+1]]]
                min_diff = diff
        
        return ans