class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])


        res=[[matrix[r][c] for r in range(row)] for c in range(col) ]

        return res