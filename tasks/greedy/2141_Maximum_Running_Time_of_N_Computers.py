class Solution:
    def maxRunTime(self, n: int, arr: list[int]) -> int:
        arr.sort()
        energy_sum = sum(arr)

        while arr[-1] > energy_sum // n:
            n -= 1
            energy_sum -= arr.pop()

        return energy_sum // n
