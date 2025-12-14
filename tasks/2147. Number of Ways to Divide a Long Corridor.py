class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 1_000_000_007

        indx = []
        for i, e in enumerate(corridor):
            if e == "S":
                indx.append(i)

        if indx == [] or len(indx) % 2 == 1:
            return 0

        count = 1

        previous_pair_last = 1
        current_pair_first = 2
        while current_pair_first < len(indx):
            count *= (indx[current_pair_first] - indx[previous_pair_last])
            count %= MOD
            previous_pair_last += 2
            current_pair_first += 2

        return count