class Solution:
    def numSteps(self, s: str) -> int:
        if len(s) == 1:
            return 0

        counter = 0
        carry = False

        for bit in reversed(s[1:]):
            if carry == True:
                if bit == "1":
                    bit = "0"
                else:
                    bit = "1"
                    carry = False
                
            if bit == "1":
                counter += 2
                carry = True
            else:
                counter += 1

        return counter + int(carry)