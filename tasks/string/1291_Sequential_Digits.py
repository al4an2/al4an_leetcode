class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        seq = "123456789"
        ans = []

        for i in range(len(seq)):
            for j in range(i+1, len(seq)+1):
                candidate = int(seq[i:j])
                if low <= candidate <= high:
                    ans.append(candidate)
        
        return sorted(ans)

