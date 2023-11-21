class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return l

        for i in range(3, numRows+1):
            tmp = []
            for j in range(i):
                if j == 0 or j == i-1:
                    tmp.append(1)
                else:
                    tmp.append(l[i-2][j-1] + l[i-2][j])
            l.append(tmp)
        return l