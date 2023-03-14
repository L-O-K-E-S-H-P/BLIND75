'''You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
step1: Transpose matrix
step2: reverse matrix
step3: print matrix
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i2 in range(len(matrix)):
            matrix[i2].reverse()
        for i1 in range(len(matrix)):
            for j1 in range(i):
                print(matrix[i1][j1],end="")
