from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        x = len(matrix)
        for item in range(0, x - 1):
            if matrix[item][0:-1] != matrix[item + 1][1:]:
                return False
        return True
