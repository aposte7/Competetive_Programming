class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        right = len(matrix) - 1
        left =0

        while right > left:
            matrix[left], matrix[right] =matrix[right],  matrix[left]
            right-=1
            left+=1

        for x in range(len(matrix) ):
            for y in range(x+1, len(matrix)):
                matrix[x][y], matrix[y][x] =  matrix[y][x], matrix[x][y]
        return matrix
            
        """
        Do not return anything, modify matrix in-place instead.
        """
        