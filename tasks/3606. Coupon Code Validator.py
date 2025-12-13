import string
class Solution:
    def validateCoupons(self, code: list[str], businessLine: list[str], isActive: list[bool]) -> list[str]:
        allowed = set(string.ascii_letters + string.digits + '_')
        priority_map = {
            "electronics":0, 
            "grocery":1, 
            "pharmacy":2, 
            "restaurant":3
            }

        results = []
        for i in range(len(code)):
            if code[i] and all(s in allowed for s in code[i]) and businessLine[i] in priority_map and isActive[i]:
                results.append((priority_map[businessLine[i]], code[i]))

        results.sort()

        return [c for _, c in results]