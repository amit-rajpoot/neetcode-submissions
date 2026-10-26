
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []

        r = len(matrix)
        c = len(matrix[0])

        top = 0
        left = 0
        bottom = r - 1
        right = c - 1

        result = []

        while top <= bottom and left <= right:

            # Left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # Top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # Right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # Bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
