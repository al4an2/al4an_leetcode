class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        n_col = len(strs[0])
        m_row = len(strs)
        count = 0
        dp_col = [1] * n_col
        for col in range(n_col):
            for col_2 in range(col):
                is_valid = True
                for row in range(m_row):
                    if strs[row][col_2] > strs[row][col]:
                        is_valid = False
                        break
                if is_valid:
                    dp_col[col] = max(dp_col[col],dp_col[col_2]+1)
            
        return n_col - max(dp_col)