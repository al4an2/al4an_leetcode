
# alternative - heap/sorting
import heapq

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}

        heap = []
        for char in s:
            if char in vowels:
                heapq.heappush(heap, char)
            

        result = []
        for char in s:
            if char in vowels:
                result.append(
                    heapq.heappop(heap))
            else:
                result.append(char)
        
        return "".join(result)

#counting
class Solution:
    def sortVowels(self, s: str) -> str:
        order = "AEIOUaeiou"
        vowels = set(order)

        idx = {ch: i for i, ch in enumerate(order)}

        counter = [0] * 10
        for char in s:
            if char in vowels:
                counter[idx[char]] += 1

        res = []
        p = 0  
        for char in s:
            if char not in vowels:
                res.append(char)
            else:
                while counter[p] == 0:
                    p += 1
                res.append(order[p])
                counter[p] -= 1

        return "".join(res)
