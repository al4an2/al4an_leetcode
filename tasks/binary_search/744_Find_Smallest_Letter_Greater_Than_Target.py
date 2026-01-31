class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if letters[0] > target:
            return letters[0]

        left, right = 0, len(letters) - 1
        result = letters[0]

        while left <= right:
            pivot = left + (right - left)//2

            if letters[pivot] > target:
                result = letters[pivot]
                right = pivot - 1
            else:
                left = pivot + 1

        return result