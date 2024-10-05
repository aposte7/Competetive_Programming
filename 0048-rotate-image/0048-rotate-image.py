class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        right = len(matrix) - 1
        left =0

        while right > left:
            for x in range(right-left):
                top ,bottom =left,right

                temp = matrix[top][left + x]
                matrix[top][left + x] = matrix[bottom - x][left]
                matrix[bottom - x][left] = matrix[bottom][right - x]
                matrix[bottom][right -x ] = matrix[top + x][right]
                matrix[top + x][right] = temp
            right-=1
            left+=1
        return matrix

