class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_1 = []
        diff_2 = []
        counter = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                counter += 1
                diff_1.append(s1[i])
                diff_2.append(s2[i])
            
        if counter == 0:
            return True
        elif counter == 2:
            if diff_1[0] == diff_2[1] and diff_1[1] == diff_2[0]:
                return True
        return False
    