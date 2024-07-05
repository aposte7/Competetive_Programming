class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row - 1):
            for x in range(1, col):
                look = matrix[i][: col - x]
                if (i+x < row) and (look != matrix[i + x][x:]):
                    return False
        return True
