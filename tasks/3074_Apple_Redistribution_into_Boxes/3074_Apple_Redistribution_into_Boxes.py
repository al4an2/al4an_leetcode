class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        s_apple = sum(apple)
        for i, el in enumerate(sorted(capacity, reverse=True)):
            s_apple -= el
            if s_apple <= 0:
                return i + 1
            
        return -1