import heapq
import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        freq_d = collections.Counter(s)

        heap = []
        for char, freq in freq_d.items():
            heapq.heappush(heap, (-freq, char))

        result = []
        while heap:
            freq, char = heapq.heappop(heap)
            result.append(char * abs(freq))

        return "".join(result)
        