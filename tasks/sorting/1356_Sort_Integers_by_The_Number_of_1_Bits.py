class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key = lambda num: (bin(num).count("1"), num))
        return arr
    
#cross bit_count
class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort(key = lambda num: (num.bit_count(), num))
        return arr