class Solution(object):
    def setZeroes(self, matrix):
        rows = []
        cols = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for row in rows:
            for m in range(len(matrix[row])):
                matrix[row][m] = 0
        for col in cols:
            for m in range(len(matrix)):
                matrix[m][col] = 0
        return matrix