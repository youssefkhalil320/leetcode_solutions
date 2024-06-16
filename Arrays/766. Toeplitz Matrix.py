class Solution:
    def isToeplitzMatrix(self, matrix):
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        # Check diagonals starting from the last row
        row = num_rows - 1
        while row >= 0:
            col = 0
            initial_value = matrix[row][col]
            row_iter = row
            while row_iter < num_rows and col < num_cols:
                if matrix[row_iter][col] != initial_value:
                    return False
                col += 1
                row_iter += 1
            row -= 1

        # Check diagonals starting from the first row
        col = 1
        while col < num_cols:
            row = 0
            initial_value = matrix[row][col]
            col_iter = col
            while col_iter < num_cols and row < num_rows:
                if matrix[row][col_iter] != initial_value:
                    return False
                row += 1
                col_iter += 1
            col += 1

        return True
