class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0]) if m > 0 else 0
        
        new_n = (m/r) * n
        if (n*m != r * c):
            return mat
        
        if new_n != c:
            return mat
        
        new_mat = []
        new_row = []
        for i in mat:
            for j in i:
                new_row.append(j)
                # print('item', j, 'New Row', new_row) 
                if len(new_row) >= c:
                    # print('Flush New Row', new_row)
                    new_mat.append(new_row)
                    new_row = []

            # print('Another row')
        
        
        return new_mat