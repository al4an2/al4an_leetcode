class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)

        left_arr = num[:n//2]
        right_arr = num[n//2:]

        left_q, right_q = 0, 0
        left_s, right_s = 0, 0

        for i in range(n//2):
            if left_arr[i] == "?":
                left_q += 1
            else:
                left_s += int(left_arr[i])
            if right_arr[i] == "?":
                right_q += 1
            else:
                right_s += int(right_arr[i])
        
        if (left_q + right_q) % 2 != 0:
            return True

        diff = left_s - right_s

        return 2 * diff != 9 * (right_q - left_q)     
