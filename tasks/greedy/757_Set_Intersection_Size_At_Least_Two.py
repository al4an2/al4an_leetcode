from typing import List
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x,: (x[0], -x[1]))
        todo = [2] * len(intervals)
        ans = 0
        while intervals:
            (s, _), t = intervals.pop(), todo.pop()
            for p in range(s, s+t):
                for i, (_ ,end) in enumerate(intervals):
                    if todo[i] and p <= end:
                        todo[i] -= 1
                ans +=1
        return ans