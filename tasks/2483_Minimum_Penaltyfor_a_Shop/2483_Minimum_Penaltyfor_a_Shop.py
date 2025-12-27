class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best_time = 0
        penalty_sum = 0
        prefix = 0

        for i in range(len(customers)):
            prefix += -1 if customers[i] == "Y" else 1

            if prefix < penalty_sum:
                penalty_sum = prefix
                best_time = i + 1

        return best_time