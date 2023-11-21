class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        m = (l+r) // 2
        
        while l < r:
            m = (l+r) // 2
            key = matrix[m][0]
            if key == target:
                return True
            mlind, mlval = None, None
            if 0 <= m - 1 < len(matrix):
                mlind, mlval = m -1, matrix[m - 1][0]
            
            mrind, mrval = None, None
            if 0 <= m + 1 < len(matrix):
                mrind, mrval = m + 1, matrix[m + 1][0]
            
            if mlind is not None and ((mlval <= target < matrix[m][0])):
                m = mlind
                break
            
            if m < len(matrix) and ((matrix[m][0] <= target < mrval)):
                break
            
            if target < key:
                r = m - 1
            else:
                l = m + 1

        l = m - 1
        r = m + 1
        row = []
        # print(l,m,r, len(matrix))
        if l >= 0 and (matrix[l][0] <= target < matrix[m][0]):
            row = matrix[l]
        elif r < len(matrix) and matrix[m][0] <= target < matrix[r][0] :
            row = matrix[m]
        else:
            if r >= len(matrix):
                row = matrix[-1]
            else:
                row = matrix[r]
        
        l = 0
        r = len(row) - 1
        m = (l+r) // 2
        # print('Row', row)
        while l <= r:
            m = (l+r) // 2
            key = row[m]
            if key == target:
                return True
            elif target < key:
                r = m - 1
            else:
                l = m + 1

        return False