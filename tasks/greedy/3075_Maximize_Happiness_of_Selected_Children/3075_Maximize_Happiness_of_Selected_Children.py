class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort(reverse = True)
        result = 0

        for i in range(k):
            child_hap = happiness[i] - i 
            if child_hap <= 0:
                break
            result += child_hap
            
        return result